const BACKEND_URL = "http://localhost:5000";

document.getElementById("form-buscar").addEventListener("submit", async (e) => {
  e.preventDefault();

  const cpf = document.getElementById("cpf").value;
  const messageDiv = document.getElementById("message");
  const resultadoDiv = document.getElementById("resultado");

  messageDiv.innerHTML = '<div class="loading">Buscando informações...</div>';
  resultadoDiv.style.display = "none";

  try {
    const response = await fetch(`${BACKEND_URL}/cidadao/buscar/${cpf}`);
    const data = await response.json();

    if (response.ok) {
      messageDiv.innerHTML = "";
      exibirResultado(data);
    } else {
      messageDiv.innerHTML = `<div class="alert alert-error">❌ ${data.erro}</div>`;
    }
  } catch (error) {
    messageDiv.innerHTML = `<div class="alert alert-error">❌ Erro de conexão: ${error.message}</div>`;
  }
});

function exibirResultado(data) {
  const resultadoDiv = document.getElementById("resultado");
  resultadoDiv.style.display = "block";

  // Dados Básicos
  const dadosBasicos = document.getElementById("dados-basicos");
  dadosBasicos.innerHTML = `
        <div class="info-item">
            <div class="info-label">Nome Completo</div>
            <div class="info-value">${data.dados_basicos.nome || "-"}</div>
        </div>
        <div class="info-item">
            <div class="info-label">CPF</div>
            <div class="info-value">${data.dados_basicos.cpf || "-"}</div>
        </div>
        <div class="info-item">
            <div class="info-label">Data de Nascimento</div>
            <div class="info-value">${formatarData(
              data.dados_basicos.data_nascimento
            )}</div>
        </div>
        <div class="info-item">
            <div class="info-label">Sexo</div>
            <div class="info-value">${data.dados_basicos.sexo || "-"}</div>
        </div>
        <div class="info-item">
            <div class="info-label">Tipo Sanguíneo</div>
            <div class="info-value">${
              data.dados_basicos.tipo_sanguineo || "-"
            }</div>
        </div>
        <div class="info-item">
            <div class="info-label">Telefone</div>
            <div class="info-value">${data.dados_basicos.telefone || "-"}</div>
        </div>
        <div class="info-item" style="grid-column: 1 / -1;">
            <div class="info-label">Endereço</div>
            <div class="info-value">${data.dados_basicos.endereco || "-"}</div>
        </div>
    `;

  // Alergias
  exibirSecao(
    "alergias",
    data.alergias,
    (alergia) => `
        <li><span class="badge">⚠️</span> ${alergia}</li>
    `
  );

  // Consultas
  exibirSecao(
    "consultas",
    data.consultas,
    (consulta) => `
        <li>
            <strong>📅 ${formatarData(consulta.data)}</strong><br>
            <strong>Médico:</strong> ${consulta.medico || "Não informado"}<br>
            <strong>Unidade:</strong> ${consulta.unidade || "Não informado"}<br>
            <strong>Relatório:</strong> ${consulta.relatorio || "Sem relatório"}
        </li>
    `
  );

  // Exames
  exibirSecao(
    "exames",
    data.exames,
    (exame) => `
        <li>
            <span class="badge">🔬</span>
            <strong>${exame.tipo}</strong><br>
            <strong>Data:</strong> ${formatarData(exame.data_realizacao)}<br>
            <strong>Local:</strong> ${exame.local || "Não informado"}<br>
            ${
              exame.link_resultado
                ? `<strong>Resultado:</strong> <a href="${exame.link_resultado}" target="_blank">Ver resultado</a>`
                : ""
            }
        </li>
    `
  );

  // Receitas
  exibirSecao(
    "receitas",
    data.receitas,
    (receita) => `
        <li>
            <span class="badge">💊</span>
            <strong>${receita.medicamento}</strong><br>
            <strong>Dosagem:</strong> ${receita.dosagem || "Não informada"}<br>
            <strong>Duração:</strong> ${receita.duracao || "Não informada"}<br>
            <strong>Data da consulta:</strong> ${formatarData(
              receita.data_consulta
            )}
        </li>
    `
  );

  // Vacinações
  exibirSecao(
    "vacinacoes",
    data.vacinacoes,
    (vacinacao) => `
        <li>
            <span class="badge">💉</span>
            <strong>${vacinacao.vacina}</strong> - Dose ${vacinacao.dose}<br>
            <strong>Data:</strong> ${formatarData(vacinacao.data_aplicacao)}<br>
            <strong>Unidade:</strong> ${vacinacao.unidade || "Não informada"}
        </li>
    `
  );

  // Cirurgias
  exibirSecao(
    "cirurgias",
    data.cirurgias,
    (cirurgia) => `
        <li>
            <span class="badge">⚕️</span>
            <strong>${cirurgia.procedimento}</strong><br>
            <strong>Data:</strong> ${formatarDataHora(
              cirurgia.data_realizacao
            )}<br>
            <strong>Duração:</strong> ${cirurgia.duracao || "Não informada"}<br>
            <strong>Hospital:</strong> ${
              cirurgia.hospital || "Não informado"
            }<br>
            ${
              cirurgia.observacoes
                ? `<strong>Observações:</strong> ${cirurgia.observacoes}<br>`
                : ""
            }
            ${
              cirurgia.cuidados
                ? `<strong>Cuidados:</strong> ${cirurgia.cuidados}`
                : ""
            }
        </li>
    `
  );

  // Internações
  exibirSecao(
    "internacoes",
    data.internacoes,
    (internacao) => `
        <li>
            <span class="badge">🛏️</span>
            <strong>Motivo:</strong> ${internacao.motivo || "Não informado"}<br>
            <strong>Entrada:</strong> ${formatarData(
              internacao.data_entrada
            )}<br>
            <strong>Alta:</strong> ${
              internacao.data_alta
                ? formatarData(internacao.data_alta)
                : "Em andamento"
            }<br>
            <strong>Ala:</strong> ${internacao.ala || "Não informada"}<br>
            <strong>Hospital:</strong> ${internacao.hospital || "Não informado"}
        </li>
    `
  );
}

function exibirSecao(nome, items, templateFn) {
  const section = document.getElementById(`section-${nome}`);
  const lista = document.getElementById(`lista-${nome}`);

  if (items && items.length > 0) {
    section.style.display = "block";
    lista.innerHTML = items.map(templateFn).join("");
  } else {
    section.style.display = "block";
    lista.innerHTML =
      '<li class="empty-message">Nenhum registro encontrado</li>';
  }
}

function formatarData(data) {
  if (!data) return "-";
  const d = new Date(data + "T00:00:00");
  return d.toLocaleDateString("pt-BR");
}

function formatarDataHora(dataHora) {
  if (!dataHora) return "-";
  const d = new Date(dataHora);
  return d.toLocaleString("pt-BR");
}
