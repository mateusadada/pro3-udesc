class Roupa {
	
	constructor() {
		// Questão 01: (Crie o construtor da classe Roupa e inicialize suas características)
		this.marca = '';
        this.cor = '';
        this.tam = 0;
        this.quant = 0;
        this.preco = 0.0;
        this.total = 0.0;
	}
	
	// Questão 02: (Crie o método get_Marca)
	get_Marca() {
        return this.marca;
    }
	
	// Questão 03: (Crie o método get_Cor)
	get_Cor() {
        return this.cor;
    }
	
	// Questão 04: (Crie o método get_Tam)
	get_Tam() {
        return this.tam;
    }
	
	// Questão 05: (Crie o método get_Quant)
	get_Quant() {
        return this.quant;
    }
	
	// Questão 06: (Crie o método get_Preco)
	get_Preco() {
        return this.preco;
    }
	
	// Questão 07: (Crie o método get_Total)
	get_Total() {
        return this.total;
    }
	
	// Questão 08: (Crie o método set_Marca)
	set_Marca(marca) {
        this.marca = marca;
    }
	
	// Questão 09: (Crie o método set_Cor)
	set_Cor(cor) {
        this.cor = cor;
    }
	
	// Questão 10: (Crie o método set_Tam)
	set_Tam(tam) {
        this.tam = tam;
    }
	
	// Questão 11: (Crie o método set_Quant)
	set_Quant(quant) {
        this.quant = quant;
    }
	
	// Questão 12: (Crie o método set_Preco)
	set_Preco(preco) {
        this.preco = preco;
    }
	
	calcula_Total() {
		// Questão 13: (Crie o método que calcula o total da compra de roupas)
		this.total = this.quant * this.preco;
	}
	
	toString() {
		// Questão 14: (Crie o método imprimir em uma string todas as
		//              características da classe Roupa)
		return `Marca: ${this.marca}\nCor: ${this.cor}\nTamanho: ${this.tam}\nQuantidade: ${this.quant}\nPreço: ${this.preco}\n\nTotal: ${this.total}\n`;
	}
}

function Limpar() {
	// Questão 15: (Construa uma função para limpar o formulário e o console na tela)
	document.getElementById('id_marca').value = '';
    document.getElementById('id_cor').value = '';
    document.getElementById('id_tam').value = '';
    document.getElementById('id_quant').value = '';
    document.getElementById('id_preco').value = '';
    document.getElementById('id_total').value = '';
    document.getElementById('id_console').value = '';
}

function Executar() {
	// Questão 16: (Extraia do formulário em tela todas as características da classe
	//              Roupa e armazene em variáveis para posterior utilização)
	var marca = document.getElementById('id_marca').value;
    var cor = document.getElementById('id_cor').value;
    var tam = document.getElementById('id_tam').value;
    var quant = parseFloat(document.getElementById('id_quant').value);
    var preco = parseFloat(document.getElementById('id_preco').value);
	
	// Questão 17: (Aloque um objeto da classe Roupa)
	var roupa = new Roupa();
	
	// Questão 18: (Insira no objeto todas as características da classe Roupa
	//              recuperadas do formulário)
	roupa.set_Marca(marca);
    roupa.set_Cor(cor);
    roupa.set_Tam(tam);
    roupa.set_Quant(quant);
    roupa.set_Preco(preco);
	
	// Questão 19: (Chame o método que calcula o total da compra de roupas)
	roupa.calcula_Total();
	
	// Questão 20: (Apresente o resultado do cálculo no componente
	//              identificado como: id_total)
	document.getElementById('id_total').value = roupa.get_Total();
	
	// Questão 21: (Chame o método que escreve em uma string todas as características
	//              da classe Roupa. Em seguida, imprima essa string no componente
	//              identificado como: id_console)
	document.getElementById('id_console').value = roupa.toString();
}
