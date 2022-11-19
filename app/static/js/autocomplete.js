// Reference: https://www.w3schools.com/howto/howto_js_autocomplete.asp


async function autocomplete(inp) {
    var cars = []
    await axios.get('/cars/')
        .then(response => {cars = response.data})
    
    // pop-up autocomplete list when user trying to type
    inp.addEventListener("click", function(e) {
        // close previous list if opened
        closeAllLists();
        row = document.createElement("DIV");
        row.setAttribute("id", this.id + "-autocomplete-list");
        row.setAttribute("class", "autocomplete-items");
        this.parentNode.appendChild(row);
        // populate the autocomplete list
        for (i = 0; i < cars.length; i++) {
            suggestion = document.createElement("DIV");
            suggestion.setAttribute("class", "text-dark");
            suggestion.textContent = cars[i];
            // auto fill the selected item
            suggestion.addEventListener("click", function(e) {
                inp.value = this.textContent.slice(0,6);
                //closeAllLists();
            });
            row.appendChild(suggestion);
        }
    });

    function closeAllLists(elmnt) {
        var x = document.getElementsByClassName("autocomplete-items");
        for (var i = 0; i < x.length; i++) {
            if (elmnt != x[i] && elmnt != inp) {
                x[i].parentNode.removeChild(x[i]);
            }
        }
    }
    // click somewhere else close the autocomplete list
    document.addEventListener("click", function (e) {
        closeAllLists(e.target);
    });
}


autocomplete(document.getElementById('car-registration-input'));
