function enableButtons() {
    updateBtn.disabled = false;
    deleteBtn.disabled = false;
}

function changeRadio(i) {
    enableButtons();
    document.getElementById(i).checked = true;
}

function findWord() {
    let word = String(document.getElementById('search').value);
    if(word.length > 0) {
        window.location.href = `/search/${word}/`;
    }
}

function findSelection() {
    let options = document.getElementsByName('selectPersonnel');
    for(let i in options){
        if(options[i].checked){
            return String(options[i].id);
        }
    }
}

function updatePerson() {
    window.location.href = `/update/${findSelection()}/`;
}
function deletePerson() {
    window.location.href = `/delete/${findSelection()}/`;
}

function printButton() {
    let pathName = window.location.pathname;
    if(pathName === '/') {
        location.href = 'export/csv/';
    } else if(pathName.substring(0,8) === '/search/') {
        location.href = '/';
        location.href = `/export/csv/${pathName.substring(8)}`;
    }
}