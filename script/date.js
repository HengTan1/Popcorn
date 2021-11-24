var element = document.querySelectorAll('[placeholder]');

for (var i in element) {
    if (element[i].nodeType == 1 && element[i].nodeName == "INPUT") {

        element[i].value = element[i].getAttribute('placeholder');
        element[i].style.color = "#777";

        element[i].onfocus = function (event) {
            if (this.value == this.getAttribute('placeholder')) {
                this.value = "";
                this.style.color = "#000"
            };
        };
        element[i].onblur = function (event) {
            if (this.value == "") {
                this.value = this.getAttribute('placeholder');
                this.style.color = "#777";
            }
        };
    }
}
