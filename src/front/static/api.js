const BACKEND_URL = "http://localhost:5000";

const schemas = {
    CIDADAO: ["cpf", "nome", "data_nasc", "sexo", "endereco", "telefone", "tipo_sanguineo"],
    ALERGIA: ["cpf", "alergia"],
    UNIDADE_SAUDE: ["cnes", "nome", "endereco", "tipo", "horario_funcinamento"],
    VACINA: ["cod", "lote", "nome_popular", "fabricante", "validade"],
    PROFISSIONAL: ["cpf", "nome", "tipo"],
    ENFERMEIRO: ["cpf", "coren"],
    MEDICO: ["cpf", "crm", "especialidade"],
    UNIDADE_BASICA_SAUDE: ["cnes"],
    HOSPITAL: ["cnes", "capacidade"],
    INTERNACAO: ["data_entrada", "cidadao", "cnes", "data_alta", "motivo", "ala_hospitalar"],
    CIRURGIA: ["data_realizacao", "cidadao", "cnes", "duracao", "observacao", "cuidados_posteriores", "nome_procedimento"],
    CONSULTA: ["data", "cidadao", "medico", "unidade_saude", "relatorio"],
    VACINACAO: ["dose", "cidadao", "vacina_cod", "vacina_lote", "ubs", "data", "enfermeiro"],
    EXAME: ["tipo", "data", "cidadao", "medico", "data_realiza", "local", "link"],
    RECEITA: ["medicamento", "data", "cidadao", "medico", "duracao", "dosagem"],
    PROFISSIONAL_ATUA_US: ["profissional", "unidade_saude"],
    MEDICO_CIRURGIA: ["data_realiza", "cidadao", "cnes", "medico"],
    ENFERMEIRO_CIRURGIA: ["data_realiza", "cidadao", "cnes", "enfermeiro"],
    PROFISSIONAL_INTERNACAO: ["data_internacao, cidadao, cnes, data_visita, horario_visita, profissional_saude, procedimento_realizado, situacao_paciente"]
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
