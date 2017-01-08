(function(){
    "strict";

    function bindby(type, className, fn){
        var elements = document.getElementsByClassName(className);
        for(var i = 0; i < elements.length; i++) {
            elements[i].addEventListener(type, fn);
        }
    }


    function clicked(event) {
        var id,
            state,
            box,
            grocery,
            el = event.currentTarget,
            current_time = Date.now();

        if(down_since !== null) {
            if(current_time - down_since > 1000) {
                return;
            }
        }

        id = el.getAttribute("id");
        box = document.getElementsByName(id)[0];
        grocery = document.getElementById("grocery_"+id);

        state = el.getAttribute("data-state");
        state = state == "False" ? "True" : "False";
        box.value = state == "True" ? 1 : 0;

        el.setAttribute("data-state", state);
        grocery.setAttribute("data-state", state);

        add2index(id);
        localStorage[id] = box.value;

        update_history(id, box.value, true);


    }

    var down_since = null;

    function mousedown(evt) {
        console.log("yup");
        down_since = Date.now();
    }

    function mouseup(evt) {
        var current_time = Date.now(),
            length = current_time - down_since;

        console.log("nope", length);
        down_since = null;
    }

    function flip_groceries(new_category) {
        var items;

        items = document.getElementsByClassName("grocery_item");

        for(let i = 0; i <items.length; i++) {
            if(items[i].getAttribute("data-cat")==new_category){
                items[i].setAttribute("data-active", "True");
            } else {
                items[i].setAttribute("data-active", "False");
            }
        }
    }

    function menuclick(evt) {
        var menu_buttons,
            el = evt.currentTarget,
            el_id = el.getAttribute("id"),
            child_id = el.getAttribute("data-dest"),
            button,
            child_panel,
            state;

        menu_buttons = document.getElementsByClassName("menu-option");
        for(var i = 0; i < menu_buttons.length; i++){
            button = menu_buttons[i];
            child_panel = document.getElementById(button.getAttribute("data-dest"));

            state = button.getAttribute("id") == el_id ? "True" : "False";
            button.setAttribute("data-active", state);
            child_panel.setAttribute("data-active", state);
        }
        flip_groceries(el.innerHTML);
    }

    function add2index(value) {
        var indexed = new Set(localStorage.indexed.split(","));
        //convoluted but it works, I guess
        indexed.add(value);
        indexed.delete("");

        localStorage.indexed = Array.from(indexed).toString();
    }

    var history_data = Array(367).fill(0);

    function update_history(id, value, push=false) {
        var position = wfmastery.json_id2pos[id];
        history_data[position] = value;

        if(push===true){
            push_history();
        }
    }

    function get_history() {
        var hash = window.location.hash.slice(1).split(","),
            version, state;

        for(let i of hash){
            if(i.startsWith("version")){
                version=i.split("=")[1];
            }
            else if(i.startsWith("state")){
                state=i.split("=")[1];
            }
        }
        return [version, state];

    }

    function push_history() {
        var hist_str = history_data.join("");
        history.pushState(null, null, `#version=1,state=${hist_str}`);
    }

    function check_history() {
        //Should only be called if localStorage is empty.
        [version_str, history_str] = get_history();

        if(!version_str || !history_str){
            return false;
        }
        history_data = history_str.split("");
        indexed = new Array();//TODO make that number a global const or something
        for(let position = 0; position < history_data.length; position++){
            indexed.concat(wfmastery.positions[position])
            localStorage[wfmastery.positions[position]] = history_data[position];
        }
        localStorage.indexed = indexed;

        return true;

    }

    function manage_storage(){

        var indexed,
            labels,
            grocery_items,
            inputs,
            data_id,
            sflag,
            nflag,
            version_str, history_str; //I am somewhat proud of this abomination

            //Generally URLS have a 1024 character limit, some browsers go up
            // much higher but assuming 1024 is probably safest.
            // So to store history data the hash history tag is formated like
            // #version={version},flags=(a 366 digit long string of 0-1's)

        if(!localStorage.indexed){
            //We are done
            localStorage.indexed = "";
            if(check_history() !== true) {
                return;
            }
        }


        indexed = localStorage.indexed.split(",");

        for (let i = 0; i < indexed.length; i++) {
            data_id = indexed[i];

            //label = document.getElementById(data_id);
            labels = document.querySelectorAll(`label[data-id='${data_id}']`)
            grocery_items = document.querySelectorAll(`.grocery_item[data-id='${data_id}']`)

            //grocery = document.getElementById("grocery_" + data_id);
            if(!labels || labels.length === 0) {
                continue;
            }

            inputs = document.getElementsByName(data_id);



            if(localStorage[data_id] > 0){
                sflag = "True"; //Prep for mixed state: False, Partial, True seems alright but will need to figure out what Partial means
                nflag = localStorage[data_id];
                update_history(data_id, localStorage[data_id]);
            } else {
                sflag = "False";
                nflag = 0;
            }
            labels.forEach(x=>{x.setAttribute("data-state", sflag)});
            grocery_items.forEach(x=>{x.setAttributes("data-state", sflag)});
            inputs.forEach(x=>{x.value=nflag});
            //label.setAttribute("data-state", sflag);
            //grocery.setAttribute("data-state", sflag);
            //input.value = nflag;
        }

        push_history();


    }



    function main(){
        var elements;
        manage_storage();

        bindby("click", "individual", clicked);
        bindby("mousedown", "individual", mousedown);
        bindby("mouseup", "individual", mouseup);

        bindby("click", "menu-option", menuclick);

        console.log(get_history());

    }

    window.addEventListener("load", main);

})();
