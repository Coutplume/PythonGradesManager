import Axios from 'axios'
export default {
    name: 'axios',
    install: function(vue){
        const axios = Axios.create({
            baseURL: 'http://localhost:5000/',
            timeout: 6000,
            withCredentials: true,
            responseType:"json",
            contentType: "application/json;charset=UTF-8"
        });
        vue.prototype.$http = axios;
    }
}