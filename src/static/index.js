const addSourceBtn = document.getElementById('add-source-btn');
const addSourceForm = document.getElementById('add-source-form');
const addFormFields = document.getElementById('add-form-fields');
const addFieldType = document.getElementById('add-field-type');
const addTagForm = document.getElementById('add-tag-form');
const addTagSourceIdInput = document.getElementById('add-tag-source-id');
const addTagNameInput = document.getElementById('tag-name');

const addSourceFormSubmitButton = document.querySelector(
    '#add-source-form button[type="submit"]',
);
const addSourceFormCloseButton = document.querySelector(
    '#add-source-form button.close',
);

const addTagFormCloseButton = document.querySelector(
    '#add-tag-form button.close',
);

const messages = document.querySelectorAll('.message');

const showAddSourceForm = () => {
    addSourceForm.classList.add('show');
    document.querySelector('#add-form-fields input').focus();
};

addSourceBtn.onclick = showAddSourceForm;

const closeAddSourceForm = () => {
    addSourceForm.classList.remove('show');
    // Hankkiutuu eroon GET-parametreista
    window.history.replaceState(null, '', window.location.pathname);
    clearSavedData();
    updateFormFields();
};

const clearSavedData = () => {
    savedFields = {};
    updateFormFields();
    fetch('/clear_session');
};

addSourceFormCloseButton.onclick = closeAddSourceForm;

window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeAddSourceForm();
        closeSourceDetails();
        closeAddTagForm();
    }
});

messages.forEach((message) => {
    message.onclick = () => message.classList.add('hide');
});

// Generoidaan lomakekentät backendistä saadun JSON-datan perusteella
const updateFormFields = () => {
    const params = new URLSearchParams(document.location.search);
    const editId = params.get('edit_id');

    const type = addFieldType.value ?? 'book';

    let allFieldsHtml = '';

    if (editId)
        allFieldsHtml += `<input type="hidden" name="edit_id" value="${editId}">`;

    for (const field of [
        ...formFields['common'],
        ...(formFields[type] ?? []),
    ]) {
        if (editId && field.name === 'bibtex_key') continue;
        const className = editId && field.name === 'bibtex_key' ? 'hide' : '';

        let friendlyName = field.name;
        const entry = content[field.name];
        if (entry) {
            friendlyName = entry[lang] ?? field.name;
        }

        const value = field.name in savedFields ? savedFields[field.name] : '';

        fieldHtml = `
<label for="add-field-${field.name}" class="${field.required ? 'required' : ''}" class="${className}">${friendlyName}</label>
<input type="${field.input_type}" name="${field.name}" placeholder="${friendlyName}" id="add-field-${field.name}" value="${value ?? ''}" class="${className}" />
`;
        allFieldsHtml += fieldHtml;
    }

    addFormFields.innerHTML = allFieldsHtml;
};

const showAddTagForm = (sourceId) => {
    addTagForm.classList.add('show');
    addTagSourceIdInput.value = sourceId;
    addTagNameInput.focus();
};

const closeAddTagForm = () => {
    addTagForm.classList.remove('show');
    addTagSourceIdInput.value = '';
};

addTagFormCloseButton.onclick = closeAddTagForm;

addFieldType.onchange = updateFormFields;
if ('kind' in savedFields) addFieldType.value = savedFields['kind'];
updateFormFields();
