(function(){
    "strict";

    function bindby(className, fn){
        var elements = document.getElementsByClassName(className);
        for(var i = 0; i < elements.length; i++) {
            elements[i].addEventListener("click", fn);
        }
    }


    function clicked(event){
        var id, state, box, el = event.currentTarget;

        id = el.getAttribute("id");
        box = document.getElementsByName(id)[0];
        state = el.getAttribute("data-state");
        state = state == "False" ? "True" : "False";
        box.value = state == "True" ? 1 : 0;

        el.setAttribute("data-state", state);

        add2index(id);
        localStorage[id] = box.value;

    }

    function menuclick(evt){
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
    }

    function add2index(value){
        var indexed = new Set(localStorage.indexed.split(","));
        //convoluted but it works, I guess
        indexed.add(value);
        indexed.delete("");

        localStorage.indexed = Array.from(indexed).toString();
    }

    function manage_storage(){

        var indexed, label, input, data_id;

        if(!localStorage.indexed){
            //We are done
            localStorage.indexed = "";
        } else{
            indexed = localStorage.indexed.split(",");


            for (let i = 0; i < indexed.length; i++) {
                data_id = indexed[i];

                label = document.getElementById(data_id);
                if(!label) {
                    continue;
                }

                input = document.getElementsByName(data_id)[0];



                if(localStorage[data_id] == "1"){
                    label.setAttribute("data-state", "True");
                    input.value = "1";
                } else {
                    label.setAttribute("data-state", "False");
                    input.value = "0";
                }
            }
        }

    }



    function main(){
        var elements;
        manage_storage();

        bindby("individual", clicked);
        bindby("menu-option", menuclick);
    }

    window.addEventListener("load", main);

})();
