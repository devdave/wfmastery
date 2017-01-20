"use strict";

/**
    "Don't reinvent the wheel"
    Sage advice except I want to know how the wheel is made and I am bored.

*/

function Abomination(input, should_wrap=false){


    var module = Abomination
        , retVal = input
        , queryStr = "";

    const NO_MATCH = Symbol();


    if(typeof input === "string" ){
        if(input.length == 0){
            console.log(`wrapper called with empty string`);
        }
        else {
            retval = module._query.call(document, input);
        }

    }
    else if(typeof input == "function") {
        //assume I meant module.Ready
        retVal = module._Ready(input)
    }
    else if(should_wrap == true) {
        retVal = module._MakeProxy(input, true);
    }
    else {
        retVal = module._MakeProxy(input, false);
    }

    console.log(retVal);
    return retVal;
}

function BuildLibrary(module, documentObject=document){


    let l_has = (obj,k)=> ((typeof obj[k] !== "undefined") && obj.hasOwnProperty(k));
    module._has = l_has;

    module._query = function m_query(input){

        let queryStr = "",
            retVal = null,
            parent = this;

        if(input[0] == "?"){
            queryStr = input.substring(1);
            retVal = parent.querySelector(queryStr);
        }
        else if(input[0] == "*"){
            queryStr = input.substring(1);
            retVal = module._MakeProxy(parent.querySelectorAll(queryStr));
        }
        else {
            console.log("Got a string without ? or * in front of it", input);
            retVal = parent.querySelector(input);
        }

        return retVal;

    }

    module._for = function(visitor){
        console.trace();
        return module._each.call(this, visitor);
    }

    module._each = function m_each(visitor){
        let count = 0, container = this;

        if(this instanceof Set){
            for(let name of this){
                visitor(name, name);
                count = count + 1;
            }
        }
        else {
            for(let name in this) {
                if(!this.hasOwnProperty(name)){
                    continue;
                }

                if(typeof this[name] == "object"){
                    visitor(module._MakeProxy(this[name]), name);
                } else {
                    visitor(this[name], name);
                }

                count = count + 1;
            }
        }

        return count;

    }



    module._on = function m_on(event, func, dom=documentObject) {

        let retVal = dom.addEventListener(event, func);
        return { cancel: ()=>dom.removeEventListener(event, func), result: retVal };
    }

    module._onOptions = function m_onWith(event, func, options={}, dom=documentObject) {
        let retVal = dom.addEventListener(event, func, options);
        return {cancel: ()=>dom.removeEventListener(event, func), result: retVal }
    }

    module._Ready = function f_Ready(func, dom=documentObject){
        return dom.addEventListener("DOMContentLoaded", func);
    }

    module._Element = function f_Element(type, recipeObj = {}, dom=documentObject) {

        let el = dom.createElement(type)
            , recipe = null
            , proxy = null;

        if(typeof recipeObj === "function"){
            recipeObj(el);
        }
        else {
            recipe = module(recipeObj, true)._each((value, name)=>{
                switch(name){
                    case "classes":
                        value._each((cls)=>el.classList.add(cls));
                        break;
                    case "attributes":
                        value._each((value, name)=>el.setAttribute(name, value));
                        break;
                    case "styles":
                        value._each((value, name)=>el.style.setProperty(name, value));
                        break;
                    default:
                        el.setAttribute(name, value);
                }

            })
        }


        return el;

    }


    module._MakeProxy = function f_MakeProxy(proxyTarget, wrap_children=false) {
        let proxyHandler = {
                get: function(target, name){


                    let retVal = target[name];

                    if(name == "_isDecorated"){
                        retVal = true;
                    }
                    else if(name[0] == "_"){
                        if(name == "_has"){
                            retVal = key=>module._has(target,key)
                        }
                        else if(name == "_raw"){
                            retVal = target;
                        }
                        else if(name == "_first") {
                            return target[0];
                        }
                        else if(module.hasOwnProperty(name)) {
                            retVal = module[name].bind(target);
                        }

                    }
                    else if(typeof target[name] == "object" && wrap_children == true){
                        retVal = module._MakeProxy(target[name]);
                    }
                    else if(typeof retVal == "function"){
                        retVal = (...args)=>{
                            let safeArgs = []
                                , bound = target[name];

                            for(var i = 0; i< args.length; i++){
                                if(args[i]._isDecorated){
                                    safeArgs.push(args[i]._raw);
                                }else{
                                    safeArgs.push(args[i]);
                                }
                            }
                            return target[name].apply(target, safeArgs);
                        }

                    }

                    console.log("get", target, name, "gave", typeof retVal);
                    return retVal;

                }
                , set: function(target, name, value, receiver) {

                    console.log("set", target, name, value, receiver);
                    if(name[0] == "_" && module._has(module, name)) {
                        throw `${name} conflicts with _ utility library`;
                    }

                    target[name] = value;



                    return true;
                }


            }

            return new Proxy(proxyTarget, proxyHandler);
    }


    return module;
};




var djw = BuildLibrary(Abomination, document);



