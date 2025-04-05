function showMoreButton(length) {
    let url = window.location.href; //url = http://127.0.0.1:5000/doctors/?d=5
    const regex = new RegExp('d=\\d+');
    const oldCount = url[url.length-1]; // oldCount = 5
    const newCount = parseInt(oldCount) + 5; // newCount = 10
    if(newCount<=length){
        url = url.replace(regex, 'd=' + newCount); //url = http://127.0.0.1:5000/doctors/?d=10
        window.location.href = url;
    }
    else {
        url = url.replace(regex, 'd=' + length);
        window.location.href = url;
    }
}

function getDoneAppointmentsButton(){
    let url = window.location.href;
    let splited = url.split('/');
    const regex = new RegExp('done=\\d+');
    if(splited[splited.length-1] === '?done=0'){
        url = url.replace(regex, 'done='+1);
    }
    console.log(url);
    window.location.href= url;
}
function getUndoneAppointmentsButton(){
    let url = window.location.href;
    let splited = url.split('/');
    const regex = new RegExp('done=\\d+');
    if(splited[splited.length-1] === '?done=1'){
        url = url.replace(regex, 'done='+0);
    }
    console.log(url);
    window.location.href= url;
}