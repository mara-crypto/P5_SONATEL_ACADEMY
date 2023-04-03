function creationComposant () {
    const composantDiv = document.createElement('div');
    composantDiv.classList.add('composant');

    const enTeteDiv = document.createElement('div');
    enTeteDiv.classList.add('enTete');

    enTeteDiv.innerHTML = "<i class='bx bxs-trash' style='color:white'></i> "
    enTeteDiv.innerHTML += "<i class='bx bxs-edit-alt' style='color:#ffffff' ></i>"
    
    composantDiv.appendChild(enTeteDiv);

    const textarea = document.createElement('textarea');
    composantDiv.appendChild(textarea);
    textarea.className="textarea"

    const iconEdit = enTeteDiv.querySelector('.bxs-edit-alt')
    iconEdit.addEventListener('click', () => {
        composantDiv.classList.toggle('edit-mode');
        textarea.disabled = !textarea.disabled;
        textarea.focus();
    });

    const iconSupp = enTeteDiv.querySelector('.bxs-trash');
    iconSupp.addEventListener('click', () => {
       componentContainer.removeChild(composantDiv);
     });


    return composantDiv ;
}

const addButton = document.getElementById('add_note');
const componentContainer = document.getElementById('composant-contenaire');

addButton.addEventListener('click', () => {
const composantt = creationComposant();
componentContainer.appendChild(composantt);
});