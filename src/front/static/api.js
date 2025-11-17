const BACKEND_URL = "http://localhost:5000";

const schemas = {
    CIDADAO: ["cpf", "nome", "data_nasc", "sexo", "endereco", "telefone", "tipo_sanguineo"],
    ALERGIA: ["cpf", "alergia"]
};

// Carrega o formulário baseado no schema
function loadForm(tabelaRaw) {
    const tabela = tabelaRaw.toUpperCase();
    const fieldsDiv = document.getElementById("fields");
    fieldsDiv.innerHTML = ""; 
    const fields = schemas[tabela];

    fields.forEach(f => {
        const label = document.createElement("label");
        label.innerText = f + ": ";

        const input = document.createElement("input");
        input.name = f;

        fieldsDiv.appendChild(label);
        fieldsDiv.appendChild(input);
        fieldsDiv.appendChild(document.createElement("br"));
    });

    document.getElementById("insertForm").onsubmit = async e => {
        e.preventDefault();

        const obj = {};
        fields.forEach(f => obj[f] = e.target[f].value);

        await fetch(`${BACKEND_URL}/${tabela}`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(obj)
        });

        alert("Inserido!");
    };
}

// Listagem de registros
async function loadTable(tabelaRaw) {
    const tabela = tabelaRaw.toUpperCase();
    const table = document.getElementById("dataTable");
    table.innerHTML = ""; 
    const data = await fetch(`${BACKEND_URL}/${tabela}`).then(r => r.json());

    if (data.length === 0) {
        table.innerHTML = "<tr><td>Sem dados</td></tr>";
        return;
    }

    // Header
    const header = document.createElement("tr");
    Object.keys(data[0]).forEach(col => {
        const th = document.createElement("th");
        th.innerText = col;
        header.appendChild(th);
    });
    table.appendChild(header);

    // Linhas
    data.forEach(row => {
        const tr = document.createElement("tr");
        Object.values(row).forEach(value => {
            const td = document.createElement("td");
            td.innerText = value;
            tr.appendChild(td);
        });
        table.appendChild(tr);
    });
}
