const BACKEND_URL = "http://localhost:5000";

const schemas = {
  CIDADAO: [
    "cpf",
    "nome",
    "data_nasc",
    "sexo",
    "endereco",
    "telefone",
    "tipo_sanguineo",
  ],
  ALERGIA: ["cpf", "alergia"],
  UNIDADE_SAUDE: ["cnes", "nome", "endereco", "tipo", "horario_funcionamento"],
  VACINA: ["cod", "lote", "nome_popular", "fabricante", "validade"],
  PROFISSIONAL: ["cpf", "nome", "tipo"],
  ENFERMEIRO: ["cpf", "coren"],
  MEDICO: ["cpf", "crm", "especialidade"],
  UNIDADE_BASICA_SAUDE: ["cnes"],
  HOSPITAL: ["cnes", "capacidade"],
  INTERNACAO: [
    "cpf_cidadao",
    "cnes_hospital",
    "data_entrada",
    "data_alta",
    "motivo",
    "ala",
  ],
  CIRURGIA: [
    "cpf_cidadao",
    "cnes_hospital",
    "data_realizacao",
    "nome_procedimento",
    "duracao",
    "observacoes",
    "cuidados",
  ],
  CONSULTA: [
    "cpf_cidadao",
    "cpf_medico",
    "data_consulta",
    "cnes_unidade",
    "relatorio_medico",
  ],
  VACINACAO: [
    "cpf_cidadao",
    "lote_vacina",
    "cod_vacina",
    "dose",
    "data_aplicacao",
    "cnes_unidade",
    "cpf_enfermeiro",
  ],
  EXAME: [
    "cpf_cidadao",
    "cpf_medico",
    "data_consulta",
    "tipo_exame",
    "data_realizacao",
    "local",
    "link_resultado",
  ],
  RECEITA: [
    "cpf_cidadao",
    "cpf_medico",
    "data_consulta",
    "medicamento",
    "dosagem",
    "duracao",
  ],
  PROFISSIONAL_ATUA_US: ["cpf_profissional", "cnes_unidade"],
  MEDICO_CIRURGIA: [
    "cpf_medico",
    "cpf_cidadao",
    "cnes_hospital",
    "data_realizacao",
  ],
  ENFERMEIRO_CIRURGIA: [
    "cpf_enfermeiro",
    "cpf_cidadao",
    "cnes_hospital",
    "data_realizacao",
  ],
  PROFISSIONAL_INTERNACAO: [
    "cpf_profissional",
    "cpf_cidadao",
    "cnes_hospital",
    "data_entrada",
    "data_hora_acompanhamento",
    "procedimentos",
    "condicao",
  ],
};

const fieldConfigs = {
  data_nasc: { type: "date", label: "Data de Nascimento" },
  data_entrada: { type: "date", label: "Data de Entrada" },
  data_alta: { type: "date", label: "Data de Alta" },
  data_consulta: { type: "date", label: "Data da Consulta" },
  data_aplicacao: { type: "date", label: "Data de Aplicação" },
  data_realizacao: {
    type: "datetime-local",
    label: "Data e Hora de Realização",
  },
  data_hora_acompanhamento: {
    type: "datetime-local",
    label: "Data e Hora do Acompanhamento",
  },
  validade: { type: "date", label: "Validade" },

  sexo: {
    type: "select",
    label: "Sexo",
    options: [
      { value: "", text: "Selecione..." },
      { value: "M", text: "Masculino" },
      { value: "F", text: "Feminino" },
      { value: "Outro", text: "Outro" },
    ],
  },
  tipo_sanguineo: {
    type: "select",
    label: "Tipo Sanguíneo",
    options: [
      { value: "", text: "Selecione..." },
      { value: "A+", text: "A+" },
      { value: "A-", text: "A-" },
      { value: "B+", text: "B+" },
      { value: "B-", text: "B-" },
      { value: "AB+", text: "AB+" },
      { value: "AB-", text: "AB-" },
      { value: "O+", text: "O+" },
      { value: "O-", text: "O-" },
    ],
  },
  tipo: {
    type: "select",
    label: "Tipo",
    options: [
      { value: "", text: "Selecione..." },
      { value: "Médico", text: "Médico" },
      { value: "Enfermeiro", text: "Enfermeiro" },
      { value: "Unidade Básica de Saúde", text: "Unidade Básica de Saúde" },
      { value: "Hospital", text: "Hospital" },
    ],
  },

  cpf: {
    type: "text",
    label: "CPF",
    maxlength: 11,
    pattern: "[0-9]{11}",
    placeholder: "Apenas números (11 dígitos)",
  },
  cpf_cidadao: {
    type: "text",
    label: "CPF do Cidadão",
    maxlength: 11,
    pattern: "[0-9]{11}",
    placeholder: "12345678901",
  },
  cpf_medico: {
    type: "text",
    label: "CPF do Médico",
    maxlength: 11,
    pattern: "[0-9]{11}",
    placeholder: "12345678901",
  },
  cpf_enfermeiro: {
    type: "text",
    label: "CPF do Enfermeiro",
    maxlength: 11,
    pattern: "[0-9]{11}",
    placeholder: "12345678901",
  },
  cpf_profissional: {
    type: "text",
    label: "CPF do Profissional",
    maxlength: 11,
    pattern: "[0-9]{11}",
    placeholder: "12345678901",
  },
  telefone: { type: "tel", label: "Telefone", placeholder: "(11) 98765-4321" },
  cnes: {
    type: "text",
    label: "CNES",
    maxlength: 20,
    placeholder: "Código da Unidade",
  },
  cnes_hospital: {
    type: "text",
    label: "CNES do Hospital",
    maxlength: 20,
    placeholder: "Código do Hospital",
  },
  cnes_unidade: {
    type: "text",
    label: "CNES da Unidade",
    maxlength: 20,
    placeholder: "Código da Unidade",
  },
  crm: { type: "text", label: "CRM", placeholder: "Registro do Médico" },
  coren: {
    type: "text",
    label: "COREN",
    placeholder: "Registro do Enfermeiro",
  },
  cod: { type: "text", label: "Código", placeholder: "Código" },
  cod_vacina: {
    type: "text",
    label: "Código da Vacina",
    placeholder: "Ex: VAC001",
  },
  lote: { type: "text", label: "Lote", placeholder: "Número do Lote" },
  lote_vacina: {
    type: "text",
    label: "Lote da Vacina",
    placeholder: "Número do Lote",
  },
  dose: { type: "number", label: "Dose", min: 1, placeholder: "1, 2, 3..." },
  capacidade: {
    type: "number",
    label: "Capacidade de Pacientes",
    min: 1,
    placeholder: "Número de leitos",
  },

  nome: { type: "text", label: "Nome Completo", placeholder: "Nome completo" },
  nome_popular: {
    type: "text",
    label: "Nome Popular",
    placeholder: "Nome conhecido da vacina",
  },
  nome_procedimento: {
    type: "text",
    label: "Nome do Procedimento",
    placeholder: "Nome da cirurgia",
  },
  fabricante: {
    type: "text",
    label: "Fabricante",
    placeholder: "Nome do fabricante",
  },
  endereco: {
    type: "text",
    label: "Endereço",
    placeholder: "Rua, número, bairro, cidade",
  },
  local: { type: "text", label: "Local", placeholder: "Local de realização" },
  ala: {
    type: "text",
    label: "Ala Hospitalar",
    placeholder: "Ex: Ala A, Enfermaria 2",
  },
  tipo_exame: {
    type: "text",
    label: "Tipo de Exame",
    placeholder: "Ex: Raio-X, Hemograma",
  },
  medicamento: {
    type: "text",
    label: "Medicamento",
    placeholder: "Nome do medicamento",
  },
  dosagem: {
    type: "text",
    label: "Dosagem",
    placeholder: "Ex: 500mg, 1 comprimido",
  },
  duracao: {
    type: "text",
    label: "Duração do Tratamento",
    placeholder: "Ex: 7 dias, 2 semanas",
  },
  especialidade: {
    type: "text",
    label: "Especialidade Médica",
    placeholder: "Ex: Cardiologia, Pediatria",
  },
  horario_funcionamento: {
    type: "text",
    label: "Horário de Funcionamento",
    placeholder: "Ex: 8h às 18h",
  },
  link_resultado: {
    type: "url",
    label: "Link do Resultado",
    placeholder: "https://...",
  },

  relatorio_medico: {
    type: "textarea",
    label: "Relatório Médico",
    placeholder: "Descreva o diagnóstico e observações...",
  },
  observacoes: {
    type: "textarea",
    label: "Observações",
    placeholder: "Observações adicionais...",
  },
  cuidados: {
    type: "textarea",
    label: "Cuidados Posteriores",
    placeholder: "Cuidados necessários após o procedimento...",
  },
  procedimentos: {
    type: "textarea",
    label: "Procedimentos Realizados",
    placeholder: "Liste os procedimentos...",
  },
  condicao: {
    type: "textarea",
    label: "Condição do Paciente",
    placeholder: "Descreva a condição atual...",
  },
  motivo: {
    type: "textarea",
    label: "Motivo",
    placeholder: "Motivo da internação ou consulta...",
  },
  alergia: {
    type: "text",
    label: "Alergia",
    placeholder: "Nome da alergia ou substância",
  },
};

function formatLabel(fieldName) {
  if (fieldConfigs[fieldName] && fieldConfigs[fieldName].label) {
    return fieldConfigs[fieldName].label;
  }
  return fieldName
    .split("_")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
}

function createInput(fieldName) {
  const config = fieldConfigs[fieldName] || { type: "text" };

  if (config.type === "select") {
    const select = document.createElement("select");
    select.name = fieldName;
    select.required = true;

    config.options.forEach((opt) => {
      const option = document.createElement("option");
      option.value = opt.value;
      option.text = opt.text;
      if (opt.value === "") option.disabled = true;
      select.appendChild(option);
    });

    return select;
  } else if (config.type === "textarea") {
    const textarea = document.createElement("textarea");
    textarea.name = fieldName;
    textarea.rows = 4;
    if (config.placeholder) textarea.placeholder = config.placeholder;
    return textarea;
  } else {
    const input = document.createElement("input");
    input.name = fieldName;
    input.type = config.type || "text";

    if (config.maxlength) input.maxLength = config.maxlength;
    if (config.pattern) {
      input.pattern = config.pattern;
      input.title = "Formato: " + config.placeholder || "";
    }
    if (config.placeholder) input.placeholder = config.placeholder;
    if (config.min !== undefined) input.min = config.min;
    if (config.type === "date" || config.type === "datetime-local") {
      if (fieldName.includes("nasc")) {
        input.max = new Date().toISOString().split("T")[0];
      }
    }

    return input;
  }
}

function loadForm(tabelaRaw) {
  const tabela = tabelaRaw.toUpperCase();
  const fieldsDiv = document.getElementById("fields");
  fieldsDiv.innerHTML = "";
  const fields = schemas[tabela];

  fields.forEach((f) => {
    const fieldWrapper = document.createElement("div");
    fieldWrapper.className = "field-wrapper";

    const label = document.createElement("label");
    label.innerText = formatLabel(f) + ":";
    label.setAttribute("for", f);

    const input = createInput(f);
    input.id = f;

    fieldWrapper.appendChild(label);
    fieldWrapper.appendChild(input);
    fieldsDiv.appendChild(fieldWrapper);
  });

  document.getElementById("insertForm").onsubmit = async (e) => {
    e.preventDefault();

    const obj = {};
    fields.forEach((f) => {
      const value = e.target[f].value;
      if (value && value.trim() !== "") {
        obj[f] = value;
      }
    });

    const messageDiv = document.getElementById("message");
    messageDiv.innerHTML = "";

    try {
      const r = await fetch(`${BACKEND_URL}/${tabela}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(obj),
      });

      if (r.ok) {
        messageDiv.innerHTML =
          '<div class="alert alert-success">Registro inserido com sucesso!</div>';
        e.target.reset();

        setTimeout(() => {
          messageDiv.innerHTML = "";
        }, 3000);
      } else {
        const error = await r.json();
        messageDiv.innerHTML = `<div class="alert alert-error">Erro: ${error.erro}</div>`;
      }
    } catch (error) {
      messageDiv.innerHTML = `<div class="alert alert-error">Erro de conexão: ${error.message}</div>`;
    }
  };
}

async function loadTable(tabelaRaw) {
  const tabela = tabelaRaw.toUpperCase();
  const table = document.getElementById("dataTable");
  const loading = document.getElementById("loading");

  table.innerHTML = "";

  try {
    const data = await fetch(`${BACKEND_URL}/${tabela}`).then((r) => r.json());

    loading.style.display = "none";
    table.style.display = "table";

    if (data.length === 0) {
      table.innerHTML =
        "<tr><td colspan='100' style='text-align: center; padding: 30px; color: #999;'>Nenhum registro encontrado</td></tr>";
      return;
    }

    const header = document.createElement("tr");
    Object.keys(data[0]).forEach((col) => {
      const th = document.createElement("th");
      th.innerText = col;
      header.appendChild(th);
    });
    table.appendChild(header);

    data.forEach((row) => {
      const tr = document.createElement("tr");
      Object.values(row).forEach((value) => {
        const td = document.createElement("td");
        td.innerText = value || "-";
        tr.appendChild(td);
      });
      table.appendChild(tr);
    });
  } catch (error) {
    loading.innerHTML = "Erro ao carregar dados: " + error.message;
    loading.style.color = "#dc3545";
  }
}
