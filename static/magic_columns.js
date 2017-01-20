class BaseColumnFilter {
        constructor(parent, position, clss){
            this.list = parent;
            this.column = {
                position: position,
                header: null,
                name: null
            };
            this.strs = {
                filtered: "data-filtered"
            }

            this.cls = clss;

            let q_str = `.${this.cls.header_row} .${this.cls.cell}:nth-child(${this.column.position})`;
            this.column.header = this.list.querySelector(q_str);
            this.column.name = this.column.header.innerHTML;

            this.reset_event = new CustomEvent("reset", {"detail": this.column.name});

            this.setup();

            this.list.addEventListener("reset", e=>{this.on_reset(e.detail)});
            this.column.header.addEventListener("click", e=>{this.show() });
        }

        setup () {
            throw "Not implemented";
        }

        show () {
            throw "Not implemented";
        }

        get_rows(only_active=true){
            let q_str = `.${this.cls.row}` + (only_active? ":not(.hide)" : "");
            return this.list.querySelectorAll(q_str);
        }

        get_cells(only_active=true) {

            let q_str = `.${this.cls.row}` + (only_active? ":not(.hide)" : "");
            q_str += ` .cell:nth-child(${this.column.position})`;
            return this.list.querySelectorAll(q_str);
        }

        is_parent(children, node) {

            let flag = false;
            while(node != null){
                flag = children.some(e=>{
                    return e === node;
                });
                if(flag === true){
                    return true;
                }
                node = node.parentElement;
            }
            return false;
        }

        is_blurred(e) {
            let is_hidden = this.box.el.classList.contains("hide") == false
                , is_block = this.box.el.style.display !== "none"
                , node = e.target;

            if( is_hidden === true || is_block === true){
                return this.is_parent([this.box.el, this.column.header], node) !== true;
            }

            return true;
        }

        all_clear(p) {
            return Array.from(p.querySelectorAll(".cell")).every(c=>c.getAttribute(this.strs.filtered) !== "true")
        }


    }

    class FilterColumn extends BaseColumnFilter {

        setup() {
            this.box = {};
            this.active_filter = null;

            this.names = new Set();


            this.get_cells(false).forEach(cell=>this.names.add(cell.innerHTML));



            this.box.el = djw._Element("div", {
                classes: ["smartbox"]
                , attributes: {
                    tabindex: "-1"
                }
                , styles: {
                    display: "none"
                    , position: "fixed"

                    , top: this.column.header.offsetTop + (this.column.header.parentElement.offsetTop)+this.column.header.offsetHeight
                    , left: this.column.header.offsetLeft + "px"
                }
            })

            this.box.cancel = document.createElement("button");
            this.box.cancel.innerHTML = "X";



            //this.box.options = document.createElement("ul");
            this.box.input = djw._Element("input",{
                attributes: {
                    list: `magic_filter_${this.column.position}`
                }
            });

            this.box.data_list = djw._Element("datalist", my_list=>{
                my_list.setAttribute("id", `magic_filter_${this.column.position}`);
                djw(this.names)._each((name)=>{
                    my_list.appendChild(djw._Element("option", {value: name}));
                });
            });


            //this.box.el.appendChild(this.box.header);
            //this.box.el.appendChild(this.box.options);

            this.box.el.appendChild(this.box.input);
            this.box.el.appendChild(this.box.data_list);
            this.box.el.appendChild(this.box.cancel);
            document.body.appendChild(this.box.el);


            this.box.cancel.addEventListener("click", e=>{ this.hide(); });
            this.box.input.addEventListener("blur", e=>{ this.hide(); });
            this.box.input.addEventListener("focusout", e=>{ this.hide() });
            this.box.input.addEventListener("input", e=>{
                this.on_select(this.box.input.value);
                this.hide();
            });


        }

        hide() {
            //this.box.options.innerHTML = "";
            this.box.el.classList.add("hide");
            //this.box.el.style.display = "none";
        }

        show() {

            this.box.el.style.display = "block";
            this.box.el.classList.remove("hide");
            this.box.input.focus();
        }

        on_select (value) {

            let flip = null;

            this.hide();
            this.active_filter = (this.active_filter === value)
                                ? ""
                                : value;


            if(this.active_filter !== ""){
                flip = c=>{
                    let should_hide = c.innerHTML != this.active_filter
                    c.setAttribute(this.strs.filtered, should_hide.toString() );
                    should_hide = (this.all_clear(c.parentElement) == false);
                    console.log(should_hide, c.parentElement, c);
                    c.parentElement.classList.toggle("hide", should_hide);
                }
            } else {
                flip = c=>{
                    c.setAttribute(this.strs.filtered, false.toString())
                    let should_hide = (this.all_clear(c.parentElement) == false);
                    c.parentElement.classList.toggle("hide", should_hide);
                }
            }

            this.get_cells(false).forEach(flip);

        }



    }

    class StringColumn extends BaseColumnFilter {


        setup(){
            this.last_value = "";

            this.box = {};

            function new_el(name, f){
                var el = document.createElement(name);
                f(el);
                return el;
            }

            this.box.cancel = djw._Element("button", el=>{
                el.innerHTML = "X";
            });

            this.box.header = djw._Element("h1", el=>{
                el.innerHTML = this.column.name;
                el.style.fontSize = this.column.header.style.fontSize;
                el.style.display = "none";
            });

            this.box.input = djw._Element("input", el=>{
                el.type = "search";
                el.size = "20";
                el.setAttribute("tabindex", "-2");
                el.name = this.column.name + "_" + "box";
            });

            this.box.el = djw._Element("div", el=>{
                el.classList.add("smartbox");

                el.style.display = "none";
                el.style.position = "fixed";
                el.style.top = this.column.header.offsetTop + (this.column.header.parentElement.offsetTop)+this.column.header.offsetHeight;
                el.style.left = this.column.header.offsetLeft;

                el.appendChild(this.box.cancel);
                el.appendChild(this.box.header);
                el.appendChild(this.box.input);
            });

            document.body.appendChild(this.box.el);


            this.box.input.addEventListener("input", e=>{ this.on_key(e); });
            this.box.input.addEventListener("blur", e=> this.hide());
            this.box.input.addEventListener("focusout", e=>this.hide());

        }


        show(e) {

            this.box.el.style.display="block";
            this.box.input.focus();

        }

        hide(e) {
            this.box.el.style.display="none";
        }

        on_key(e) {

            let value = e.target.value.trim();
            let visitor = v=>{true};
            let flag = false;

            if(value === this.last_value){
                return;
            }

            this.last_value = value;

            let toggle_row = (c, should_hide)=>{
                c.setAttribute(this.strs.filtered, should_hide.toString());
                c.parentElement.classList.toggle("hide", this.all_clear(c.parentElement) == false );


            }

            //Is it a regex?
            if(value.startsWith("/") && value.indexOf("/") != value.lastIndexOf("/")) {
                console.log("is regex");

                let body = value.slice(1, value.lastIndexOf("/"));

                let regex_flag = value.endsWith("/") ? "" : value.slice(value.lastIndexOf("/")+1);

                console.log(body, regex_flag);
                let rx = new RegExp(body, regex_flag);
                visitor = c=>{
                    toggle_row(c, c.innerHTML.match(rx) === null)
                }
            }
            else if(value === "") {
                console.log("clear column filter");
                visitor = c=>{
                    toggle_row(c, false)
                }
            }
            else {
                console.log("brute force")
                visitor = c=>{
                    toggle_row(c, c.innerHTML.includes(value) !== true);
                }
            }

            this.get_cells(false).forEach(visitor);

        }

    }
