
const zone = document.getElementById("zone");


const zoneBlanc = document.createElement('div');
zoneBlanc.id = "zoneBlanc" ;
zone.appendChild(zoneBlanc);

const zoneDeNotification = document.createElement("div")
zoneDeNotification.id = "zoneDeNotification";
zone.appendChild(zoneDeNotification);



const notificationSuccess = document.createElement("div");
notificationSuccess.id = "notificationSuccess";
notificationSuccess.innerHTML = "<p>Notification Success</p>" ;
zoneBlanc.appendChild(notificationSuccess);


notificationSuccess.addEventListener("click", function() {
    const text = document.createElement("div")
    text.id = "notificationSuccess"
    text.innerHTML = "<p>Success</p>";
    zoneDeNotification.appendChild(text);
    setTimeout(function() {
        zoneDeNotification.removeChild(text);
    },2000)     
})




const notificationDanger = document.createElement("div");
notificationDanger.id = "notificationDanger" ;
notificationDanger.innerHTML = "<p>Notification Danger</p>";
zoneBlanc.appendChild(notificationDanger);


notificationDanger.addEventListener("click", function() {
    const text = document.createElement("div")
    text.id = "notificationDanger"
    text.innerHTML = "<p>Attention</p>";
    zoneDeNotification.appendChild(text);
    setTimeout(function() {
        zoneDeNotification.removeChild(text);
    },2000)
})


const notificationWarning = document.createElement("div");
notificationWarning.id = "notificationWarning"
notificationWarning.innerHTML = "<p>Notification Warning</p>";
zoneBlanc.appendChild(notificationWarning);


notificationWarning.addEventListener("click", function() {
    const text = document.createElement("div")
    text.id = "notificationWarning"
    text.innerHTML = "<p>Avertissement</p>";
    zoneDeNotification.appendChild(text);
    setTimeout(function() {
        zoneDeNotification.removeChild(text);
    },2000)

        
})

const notificationInfo = document.createElement("div");
notificationInfo.id = "notificationInfo"
notificationInfo.innerHTML = "<p>Notification Info</p>";
zoneBlanc.appendChild(notificationInfo);


notificationInfo.addEventListener("click", function() {
    const text = document.createElement("div")
    text.id = "notificationInfo"
    text.innerHTML = "<p>Info</p>";
    zoneDeNotification.appendChild(text);
    setTimeout(function() {
        zoneDeNotification.removeChild(text);
    },2000)

        
})
