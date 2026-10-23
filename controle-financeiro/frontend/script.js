
const dinheiro = valor =>
    Number(valor).toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL"
    });

async function carregarResumo() {
    const resposta = await fetch("/resumo");

    if (!resposta.ok) {
        throw new Error("Não foi possível carregar o resumo.");
    }

    const dados = await resposta.json();

    document.getElementById("saldo").textContent =
        dinheiro(dados.saldo);

    document.getElementById("receitas").textContent =
        dinheiro(dados.total_receitas);

    document.getElementById("despesas").textContent =
        dinheiro(dados.total_despesas);
}

async function carregarTransacoes() {
    const resposta = await fetch("/transacoes");

    if (!resposta.ok) {
        throw new Error("Não foi possível carregar as transações.");
    }

    const transacoes = await resposta.json();
    const lista = document.getElementById("lista-transacoes");

    lista.replaceChildren();

    transacoes.forEach(transacao => {
        const linha = document.createElement("tr");

        const valores = [
            transacao.descricao,
            transacao.tipo,
            dinheiro(transacao.valor),
            transacao.categoria
        ];

        valores.forEach((valor, indice) => {
            const celula = document.createElement("td");
            celula.textContent = valor;

            if (indice === 1) {
                celula.className =
                    transacao.tipo === "receita"
                        ? "tipo-receita"
                        : "tipo-despesa";
            }

            linha.appendChild(celula);
        });

        lista.appendChild(linha);
    });
}

async function atualizarPainel() {
    try {
        await Promise.all([
            carregarResumo(),
            carregarTransacoes()
        ]);
    } catch (erro) {
        document.getElementById("mensagem").textContent =
            erro.message;
    }
}

document.getElementById("form-transacao")
    .addEventListener("submit", async evento => {
        evento.preventDefault();

        const mensagem = document.getElementById("mensagem");

        const transacao = {
            descricao: document.getElementById("descricao").value.trim(),
            tipo: document.getElementById("tipo").value,
            valor: Number(document.getElementById("valor").value),
            categoria: document.getElementById("categoria").value.trim()
        };

        try {
            const resposta = await fetch("/transacoes", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(transacao)
            });

            if (!resposta.ok) {
                const erro = await resposta.json();
                throw new Error(
                    erro.detail
                        ? JSON.stringify(erro.detail)
                        : "Confira os dados e tente novamente."
                );
            }

            mensagem.textContent = "Transação cadastrada com sucesso!";
            document.getElementById("form-transacao").reset();

            await atualizarPainel();
        } catch (erro) {
            mensagem.textContent = "Erro: " + erro.message;
        }
    });

atualizarPainel();
