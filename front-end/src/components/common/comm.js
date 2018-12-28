import Vue from 'vue';

let MyComm = new Vue({
    methods: {
        deleteCookie: function (cname) {
            let d = new Date();
            let expires = "expires=" + d.toGMTString();
            document.cookie = cname + "=; " + expires;
        },

        getCookie: function (cname) {
            let name = cname + "=";
            let ca = document.cookie.split(';');
            for (let i = 0; i < ca.length; i++) {
                let c = ca[i].trim();
                if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
            }
            return "";
        },

        setCookie: function (cname, cvalue, exdays) {
            let d = new Date();
            d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
            let expires = "expires=" + d.toGMTString();
            document.cookie = cname + "=" + cvalue + "; " + expires;
        }
    },
    data: {
    }
})

export default MyComm;
Vue.prototype.$MyComm = MyComm;
