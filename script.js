"use strict";

(function(){
    "use strict";


    var History_data = new Array(367).fill(0),
        down_since = -1,
        is_down = false;


    function bindbyclass(type, className, fn){
        /*
            Connect a handler to a specific event
        */
        var elements = document.getElementsByClassName(className);
        for(var i = 0; i < elements.length; i++) {
            elements[i].addEventListener(type, fn);
        }
    }


    function change_attribute(data_id, str_flag, number_flag) {
        /**
            To avoid repeating myself over and over
            consolidates changing all relevant elements by
        */
        var labels, grocery_items;

        labels = document.querySelectorAll(`label[data-id='${data_id}']`);
        grocery_items = document.querySelectorAll(`.grocery_item[data-id='grocery_${data_id}']`);


        labels.forEach(x=>{x.setAttribute("data-state", str_flag);});
        grocery_items.forEach(x=>{x.setAttribute("data-state", str_flag);});
        //inputs.forEach(x=>{x.value=number_flag});
    }


    //function clicked(element) {
    //    var data_id,
    //        current_time = Date.now(),
    //        str_flag, num_flag;
    //
    //    data_id = element.getAttribute("id");
    //
    //    str_flag = element.getAttribute("data-state");
    //    str_flag = (str_flag == "False" ? "True" : "False");
    //    num_flag = (str_flag == "True" ? 1 : 0);
    //
    //    change_attribute(data_id, str_flag, num_flag);
    //
    //    Storage.Set(data_id, num_flag);
    //    History.update(data_id, num_flag, true);
    //}


    function mousedown(evt) {
        var element = evt.currentTarget,
            data_id = element.getAttribute("data-id"),
            current_state = element.getAttribute("data-state"),
            down_since;

        is_down = true;

        window.setTimeout(_=>{
            checker(data_id, Date.now(), current_state, element);
        }, 100);

    }

    function checker(data_id, down_since, current_state, element){
        var length = Date.now() - down_since,
            new_state = null,
            num_flag = 0;

        if(is_down === true) {
            if(length >= 1000) {
                switch(current_state) {
                    case "True":
                    case "False":
                        new_state = "Partial";
                        num_flag = 2;
                        break;
                    default:
                        new_state = "False";
                        num_flag = 0;
                        break;
                }
                is_down = false;
            } else {
                window.setTimeout(_=>{
                    checker(data_id, down_since, current_state, element);
                }, 100);
            }
        } else {
            switch(current_state) {
                case "Partial":
                case "True":
                    new_state = "False";
                    num_flag = 0;
                    break;
                default:
                    new_state = "True";
                    num_flag = 1;
            }
        }

        if(new_state !== null) {
            change_attribute(data_id, new_state, num_flag);
            Storage.Set(data_id, num_flag);
            History.update(data_id, num_flag, true);
        }

    }

    function mouseup(evt) {
        is_down = false;
        down_since = -1;
    }

    function show_or_hide_groceries(new_category) {
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
        show_or_hide_groceries(el.innerHTML);
    }


    class Storage {


        static Index_as_string(){
            if(window.localStorage.indexed === undefined){
                window.localStorage.indexed = [];
            }

            return window.localStorage.indexed;
        }

        static Index_as_array(){
            var temp;

            temp = Storage.Index_as_string().split(",");
            if(temp.length > 0 && temp[0] === "") {
                //note this is really starting to piss me off
                temp.shift();
            }
            return temp;

        }

        static Index_as_set() {
            return new Set(Storage.Index_as_array());
        }

        static Set(identifier, value) {
            var add2index = false,
                index = Storage.Index_as_set();

            index.add(identifier);
            window.localStorage.indexed = [...index].toString();

            window.localStorage[identifier] = value;
        }

        static Get(identifier) {
            return window.localStorage[identifier];
        }



    }


    class History {
        //Generally URLS have a 1024 character limit, some browsers go up
        // much higher but assuming 1024 is probably safest.
        // So to store history data the hash history tag is formated like
        // #version={version},flags=(a 366 digit long string of 0-1's)



        static setup(){
            History_data = new Array(367).fill(0);
        }

        static update(id, value, push=false){
            var position = wfmastery.json_id2pos[id];
            History_data[position] = value;

            if(push===true){
                History.push();
            }

        }

        static check() {
            //Should only be called if localStorage is empty.
            var indexed, version_st, version_str, history_str, history_arr;

            [version_str, history_str] = History.get();

            if(!version_str || !history_str){
                return false;
            }

            history_arr = history_str.split("");

            indexed = [];
            for(let position = 0; position < history_arr.length; position++){
                Storage.Set(wfmastery.positions[position], history_arr[position]);
            }

            return true;
        }

        static get() {
            var hash, version, state;

            hash = window.location.hash.slice(1).split(",");

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

        static push() {
            var hist_str;
            hist_str = History_data.join("");
            window.history.pushState(null, null, `#version=1,state=${hist_str}`);
        }

    }


    function reload(){

        var index,
            labels,
            grocery_items,
            inputs,
            data_id,
            sflag,
            nflag,
            version_str, history_str; //I am somewhat proud of this abomination


        index = Storage.Index_as_array();


        if(index.length === 0){
            //We are done
            if(History.check() !== true) {
                return;
            }
        }




        for (let i = 0; i < index.length; i++) {
            data_id = index[i];

            labels = document.querySelectorAll(`label[data-id='${data_id}']`);

            if(!labels || labels.length === 0) {
                continue;
            }

            nflag = Storage.Get(data_id);

            if(nflag === null) {
                nflag = 0;
                History.set(data_id, nflag);
            }

            switch(nflag) {
                case "1":
                case 1:
                    sflag="True";
                    break;
                case "2":
                case 2:
                    sflag="Partial";
                    break;
                default:
                    sflag="False";
                    break;
            }

            change_attribute(data_id, sflag, nflag);

        }

    }



    function main(){
        var elements;
        History.setup();
        reload();

        //bindbyclass("click", "individual", clicked);
        bindbyclass("mousedown", "individual", mousedown);
        bindbyclass("mouseup", "individual", mouseup);
        bindbyclass("click", "menu-option", menuclick);

    }

    window.addEventListener("load", main);

})();
