class AtividadeFisica {
	
	constructor() {
		// Questão 01: (Crie o construtor da classe AtividadeFisica e
		//              inicialize as suas características)
		this.cic_masc = 0.0;
        this.cic_fem = 0.0;
        this.cor_masc = 0.0;
        this.cor_fem = 0.0;
        this.nat_masc = 0.0;
        this.nat_fem = 0.0;
        this.tot_cal_masc = 0.0;
        this.tot_cal_fem = 0.0;
	}
	
	// Questão 02: (Crie o método get_cic_masc)
	get_cic_masc() { return this.cic_masc; }
	
	// Questão 03: (Crie o método get_cic_fem)
	get_cic_fem() { return this.cic_fem; }
	
	// Questão 04: (Crie o método get_cor_masc)
	get_cor_masc() { return this.cor_masc; }
	
	// Questão 05: (Crie o método get_cor_fem)
	get_cor_fem() { return this.cor_fem; }
	
	// Questão 06: (Crie o método get_nat_masc)
	get_nat_masc() { return this.nat_masc; }
	
	// Questão 07: (Crie o método get_nat_fem)
	get_nat_fem() { return this.nat_fem; }
	
	// Questão 08: (Crie o método get_tot_cal_masc)
	get_tot_cal_masc() { return this.tot_cal_masc; }
	
	// Questão 09: (Crie o método get_tot_cal_fem)
	get_tot_cal_fem() { return this.tot_cal_fem; }
	
	//
	
	// Questão 10: (Crie o método set_cic_masc)
	set_cic_masc(cm0) { this.cic_masc = cm0; }
	
	// Questão 11: (Crie o método set_cic_fem)
	set_cic_fem(cf0) { this.cic_fem = cf0; }
	
	// Questão 12: (Crie o método set_cor_masc)
	set_cor_masc(cm0) { this.cor_masc = cm0; }
	
	// Questão 13: (Crie o método set_cor_fem)
	set_cor_fem(cf0) { this.cor_fem = cf0; }
	
	// Questão 14: (Crie o método set_nat_masc)
	set_nat_masc(nm0) { this.nat_masc = nm0; }
	
	// Questão 15: (Crie o método set_nat_fem)
	set_nat_fem(nf0) { this.nat_fem = nf0; }
	
	// Questão 16: (Crie o método set_tot_cal_masc)
	set_tot_cal_masc(tcm0) { this.tot_cal_masc = tcm0; }
	
	// Questão 17: (Crie o método set_tot_cal_fem)
	set_tot_cal_fem(tcf0) { this.tot_cal_fem = tcf0; }
	
	calculo() {
		// Questão 18:  (Crie o método que realiza os seguintes cálculos:
        //               o total de calorias gastas nas atividades físicas masculinas,
        //               o total de calorias gastas nas atividades físicas femininas)
		this.tot_cal_masc = this.cic_masc + this.cor_masc + this.nat_masc;
		this.tot_cal_fem = this.cic_fem + this.cor_fem + this.nat_fem;
	}
	
	toString() {
		// Questão 19: (Crie o método para imprimir em uma string todas as
		//              características da classe AtividadeFisica)
		return `Ciclismo masculino: ${this.cic_masc.toFixed(2)}\n` +
		`Corrida masculino: ${this.cor_masc.toFixed(2)}\n` +
		`Natação masculino: ${this.nat_masc.toFixed(2)}\n` +
		`Total calorias masculino: ${this.tot_cal_masc.toFixed(2)}\n\n` +
		`Ciclismo feminino: ${this.cic_fem.toFixed(2)}\n` +
		`Corrida feminino: ${this.cor_fem.toFixed(2)}\n` +
		`Natação feminino: ${this.nat_fem.toFixed(2)}\n` +
		`Total calorias feminino: ${this.tot_cal_fem.toFixed(2)}\n`;
	}
}

function Limpar() {
	// Questão 20: (Construa uma função para limpar os formulários e o console na tela)
	document.getElementById("id_cic_masc").value = "";
    document.getElementById("id_cic_fem").value = "";
    document.getElementById("id_cor_masc").value = "";
    document.getElementById("id_cor_fem").value = "";
    document.getElementById("id_nat_masc").value = "";
    document.getElementById("id_nat_fem").value = "";
    document.getElementById("id_tot_cal_masc").value = "";
    document.getElementById("id_tot_cal_fem").value = "";
    document.getElementById("id_console").value = "";
}

function Executar() {
	// Questão 21: (Extraia do formulário em tela todas as características da classe
	//              AtividadeFisica e armazene em variáveis para posterior utilização)
	let cic_masc = parseFloat(document.getElementById("id_cic_masc").value) || 0.0;
    let cic_fem = parseFloat(document.getElementById("id_cic_fem").value) || 0.0;
    let cor_masc = parseFloat(document.getElementById("id_cor_masc").value) || 0.0;
    let cor_fem = parseFloat(document.getElementById("id_cor_fem").value) || 0.0;
    let nat_masc = parseFloat(document.getElementById("id_nat_masc").value) || 0.0;
    let nat_fem = parseFloat(document.getElementById("id_nat_fem").value) || 0.0;
	
	// Questão 22: (Aloque um objeto da classe AtividadeFisica)
	let atividade = new AtividadeFisica();
	
	// Questão 23: (Insira no objeto todas as características da classe AtividadeFisica
	//              recuperadas do formulário)
	atividade.set_cic_masc(cic_masc);
    atividade.set_cic_fem(cic_fem);
    atividade.set_cor_masc(cor_masc);
    atividade.set_cor_fem(cor_fem);
    atividade.set_nat_masc(nat_masc);
    atividade.set_nat_fem(nat_fem);
	
	// Questão 24: (Chame o método que realiza todos os cálculos citados na Questão 18)
	atividade.calculo();
	
	// Questão 25: (Apresente o resultado dos cálculos nos componentes
	//              identificados como: "id_tot_cal_masc" e "id_tot_cal_fem")
	document.getElementById("id_tot_cal_masc").value = atividade.get_tot_cal_masc().toFixed(2);
    document.getElementById("id_tot_cal_fem").value = atividade.get_tot_cal_fem().toFixed(2);
	
	// Questão 26: (Chame o método que escreve em uma string todas as características
	//              da classe AtividadeFisica. Em seguida, imprima essa string no
	//              componente identificado como: "id_console")
	document.getElementById("id_console").value = atividade.toString();
}
