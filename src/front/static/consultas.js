const BACKEND_URL = "http://localhost:5000";

// Função auxiliar para criar tabela de resultados
function createResultTable(data, containerId) {
  const container = document.getElementById(containerId);

  if (!data || data.length === 0) {
    container.innerHTML =
      '<div class="alert alert-error">📭 Nenhum resultado encontrado</div>';
    return;
  }

  let html = "<table><tr>";

  // Headers
  data[0].forEach((_, index) => {
    html += `<th>Coluna ${index + 1}</th>`;
  });
  html += "</tr>";

  // Rows
  data.forEach((row) => {
    html += "<tr>";
    row.forEach((cell) => {
      html += `<td>${cell || "-"}</td>`;
    });
    html += "</tr>";
  });

  html += "</table>";
  container.innerHTML = html;
}

// Consulta 1: Histórico do Cidadão
document
  .getElementById("form-historico")
  .addEventListener("submit", async (e) => {
    e.preventDefault();
    const cpf = e.target.cpf.value;
    const container = document.getElementById("result-historico");

    container.innerHTML = '<div class="loading">Carregando...</div>';

    try {
      const response = await fetch(
        `${BACKEND_URL}/consultas/historico_cidadao/${cpf}`
      );
      const data = await response.json();

      if (response.ok) {
        createResultTable(data, "result-historico");
      } else {
        container.innerHTML = `<div class="alert alert-error">Erro: ${data.erro}</div>`;
      }
    } catch (error) {
      container.innerHTML = `<div class="alert alert-error">Erro de conexão: ${error.message}</div>`;
    }
  });

// Consulta 2: Vacinas em Atraso
document
  .getElementById("form-vacinas")
  .addEventListener("submit", async (e) => {
    e.preventDefault();
    const ano = e.target.ano.value;
    const vacina = e.target.vacina.value;
    const container = document.getElementById("result-vacinas");

    container.innerHTML = '<div class="loading">Carregando...</div>';

    try {
      const response = await fetch(
        `${BACKEND_URL}/consultas/vacinas_atraso?ano=${ano}&vacina=${vacina}`
      );
      const data = await response.json();

      if (response.ok) {
        createResultTable(data, "result-vacinas");
      } else {
        container.innerHTML = `<div class="alert alert-error">Erro: ${data.erro}</div>`;
      }
    } catch (error) {
      container.innerHTML = `<div class="alert alert-error">Erro de conexão: ${error.message}</div>`;
    }
  });

// Consulta 3: Consultas por Unidade
document
  .getElementById("form-unidade")
  .addEventListener("submit", async (e) => {
    e.preventDefault();
    const inicio = e.target.inicio.value;
    const fim = e.target.fim.value;
    const container = document.getElementById("result-unidade");

    container.innerHTML = '<div class="loading">Carregando...</div>';

    try {
      const response = await fetch(
        `${BACKEND_URL}/consultas/consultas_unidade?inicio=${inicio}&fim=${fim}`
      );
      const data = await response.json();

      if (response.ok) {
        createResultTable(data, "result-unidade");
      } else {
        container.innerHTML = `<div class="alert alert-error">Erro: ${data.erro}</div>`;
      }
    } catch (error) {
      container.innerHTML = `<div class="alert alert-error">Erro de conexão: ${error.message}</div>`;
    }
  });

// Consulta 4: Pacientes por Medicamento
document
  .getElementById("form-medicamento")
  .addEventListener("submit", async (e) => {
    e.preventDefault();
    const medicamento = e.target.medicamento.value;
    const container = document.getElementById("result-medicamento");

    container.innerHTML = '<div class="loading">Carregando...</div>';

    try {
      const response = await fetch(
        `${BACKEND_URL}/consultas/pacientes_medicamento/${encodeURIComponent(
          medicamento
        )}`
      );
      const data = await response.json();

      if (response.ok) {
        createResultTable(data, "result-medicamento");
      } else {
        container.innerHTML = `<div class="alert alert-error">Erro: ${data.erro}</div>`;
      }
    } catch (error) {
      container.innerHTML = `<div class="alert alert-error">Erro de conexão: ${error.message}</div>`;
    }
  });

// Consulta 5: Cidadãos com Todas as Vacinas
async function buscarTodasVacinas() {
  const container = document.getElementById("result-todas-vacinas");
  container.innerHTML = '<div class="loading">Carregando...</div>';

  try {
    const response = await fetch(
      `${BACKEND_URL}/consultas/cidadaos_todas_vacinas`
    );
    const data = await response.json();

    if (response.ok) {
      createResultTable(data, "result-todas-vacinas");
    } else {
      container.innerHTML = `<div class="alert alert-error">Erro: ${data.erro}</div>`;
    }
  } catch (error) {
    container.innerHTML = `<div class="alert alert-error">Erro de conexão: ${error.message}</div>`;
  }
}
