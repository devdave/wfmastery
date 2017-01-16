/* jshint esnext: true */

class StorageCls {
    /**
        unfortunately Komodo doesn't see this
    */
    constructor (src) {
        this.src = src;
    }

    index_as_string() {
        if(this.src.indexed === undefined){
            this.src.indexed = [];
        }

        return this.src.indexed;
    }

    index_as_array() {
        var temp;

        temp = this.index_as_string().split(",");
        if(temp.length > 0 && temp[0] === "") {
            //note this is really starting to piss me off
            temp.shift();
        }
        return temp;

    }

    index_as_set() {
        return new Set(this.index_as_array());
    }

    set(identifier, value) {
        var add2index = false,
            index = this.index_as_set();

        index.add(identifier);
        this.src.indexed = [...index].toString();
        this.src[identifier] = value;
    }

    get(identifier) {
        return this.src[identifier];
    }



}


class HistoryCls {
    //Generally URLS have a 1024 character limit, some browsers go up
    // much higher but assuming 1024 is probably safest.
    // So to store history data the hash history tag is formated like
    // #version={version},flags=(a 366 digit long string of 0-1's)

    constructor (master_data, history_size=380, history_version=-1){
        this.master = master_data;
        this.version = history_version;
        this.data = new Array(history_size).fill(0);
    }

    update(id, value, push=false){
        var position = this.master.json_id2pos[id];
        this.data[position] = value;

        if(push===true){
            this.push();
        }

    }

    check(storage) {
        //Should only be called if localStorage is empty.
        var indexed, version_st, version_str, history_str, history_arr;

        [version_str, history_str] = this.get();

        if(!version_str || !history_str){
            return false;
        }

        history_arr = history_str.split("");

        indexed = [];
        for(let position = 0; position < history_arr.length; position++){
            storage.set(this.master.positions[position], history_arr[position]);
        }

        return true;
    }

    decompress(hash_str) {
        var new_str = hash_str;
        return new_str;
    }

    compress(hash_str) {
        var new_str = hash_str;
        return new_str;
    }

    get() {
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

    push() {
        var hist_str;
        hist_str = this.data.join("");
        window.history.pushState(null, null, `#version=${this.version},state=${hist_str}`);
    }

}

class ClickHandler {
    constructor (app, history, storage){
        this.app = app;
        this.history = history;
        this.storage = storage;
        this.is_down = false;
    }

    down(evt) {

        var element = evt.currentTarget,
            data_id = element.getAttribute("data-id"),
            current_state = element.getAttribute("data-state");

        if(evt.button !== 0) {
            console.log(evt.button);
            return;
        }

        this.is_down = true;

        window.setTimeout(_=>{
            this.checker(data_id, Date.now(), current_state, element);
        }, 100);

    }

    up(evt) {
        this.is_down = false;
    }


    checker(data_id, down_since, current_state, element){
        var length = Date.now() - down_since,
            new_state = null,
            num_flag = 0;

        if(this.is_down === true) {
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
                this.is_down = false;
            } else {
                window.setTimeout(_=>{
                    this.checker(data_id, down_since, current_state, element);
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
            this.app.change_attribute(data_id, new_state, num_flag);
            this.storage.set(data_id, num_flag);

            this.history.update(data_id, num_flag, true);
        }
    }
}


(function(){
    "use strict";


    //var history, storage,
    //    down_since = -1,
    //    is_down = false;


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
            consolidates changing all relevant elements
        */
        document
            .querySelectorAll(`label[data-id='${data_id}']`)
            .forEach(x=>{x.setAttribute("data-state", str_flag);});

        document
            .querySelectorAll(`.grocery_item[data-id='grocery_${data_id}']`)
            .forEach(x=>{x.setAttribute("data-state", str_flag);});

    }





    function show_or_hide_groceries(new_category) {


        document
            .querySelectorAll(".grocery_block")
            .forEach(x=>{
                if(x.getAttribute("data-cat")==new_category) {
                    x.setAttribute("data-active", "True");
                }
                else {
                    x.setAttribute("data-active", "False");
                }
            });

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
        show_or_hide_groceries(el.getAttribute("data-dest"));
    }


    function reload(storage, history){

        var index,
            labels,
            grocery_items,
            inputs,
            data_id,
            sflag,
            nflag,
            version_str, history_str; //I am somewhat proud of this abomination


        index = storage.index_as_array();


        if(index.length === 0){
            //We are done
            if(history.check(storage) !== true) {
                return;
            }
        }

        for (let i = 0; i < index.length; i++) {
            data_id = index[i];

            labels = document.querySelectorAll(`label[data-id='${data_id}']`);

            if(!labels || labels.length === 0) {
                continue;
            }

            nflag = storage.get(data_id);

            if(nflag === null) {
                nflag = 0;

            }

            history.update(data_id, nflag);

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
            history.push();

        }

    }



    function main(){
        var elements, history, storage, click_handler, app;

        history = new HistoryCls(wfmastery, wfmastery.total_size, 2);
        storage = new StorageCls(window.localStorage);

        app = { change_attribute };

        click_handler = new ClickHandler(app, history, storage);

        reload(storage, history);

        bindbyclass("mousedown", "individual", evt=> click_handler.down(evt));
        bindbyclass("mouseup", "individual", evt=> click_handler.up(evt));

        bindbyclass("click", "menu-option", menuclick);

    }

    window.addEventListener("load", main);

})();
