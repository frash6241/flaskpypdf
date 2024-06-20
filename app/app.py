from flask import Flask, render_template,request, redirect, url_for,flash
from flask_mysqldb import MySQL
from PyPDF2 import PdfReader
from werkzeug.utils import secure_filename
import os
import re
import pandas as pad
from datetime import datetime
from dateutil import parser

app = Flask(__name__)

#Iniciar las listas
nomb = ""
eda = ""
pes = ""
alt = ""
fecha_na = ""
sex = ""
tel = ""
cel = ""
obra_s = ""
tipo_p = ""
ejerc = ""
numero_a = ""
#Datos personales
fecha_es = ""
med_o = ""
med_d = ""
protocolo = ""
observaciones = ""
#Interrogatorio previo
motivo = ""
antecedentes = ""
fac_riesgo = ""
habitual = ""
minuto = ""
carga = ""
ECG = ""
ECO = ""
Septum = ""
Pared_posterior = ""
DFD = ""
DFS = ""
IMVI = ""
Terapia_anti = ""
Prueba_bajo = ""
FCMP = ""
FCMP_porcentaje = ""
#Reserva Coronaria
VFCB = ""
VFCMax = ""
RCD = ""
Alt_ECG = ""
isquemia = ""
#Test detenido por efectos adversos
test_ad =""
motivo_test = ""
Tiempo_inicio = ""

diagnostico = ""
conclusiones = ""

#CONEXION A LA BASE DE DATOS
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'diario_bd'
mysql = MySQL(app)

#SESSION 
app.secret_key = 'mysecretkey'

ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = 'static/uploads'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def acortar_texto(texto, max_length=20):
    if len(texto) <= max_length:
       return texto
    return texto[:max_length-3] + '...' 

@app.route('/')
def Index():
	cur = mysql.connection.cursor()
	cur.execute('SELECT * FROM datos_estudio ORDER BY id DESC')
	data = cur.fetchall()
	return render_template('index.html', pdf = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
	if request.method == 'POST':
		fullname = request.form['fullname']
		phone = request.form['phone']
		email = request.form['email']
		cur = mysql.connection.cursor()
		cur.execute('INSERT INTO datospdf (fullname , phone, email) VALUES(%s, %s, %s)',
		(fullname, phone, email))
		mysql.connection.commit()
		flash('Se insertado correctamente')
	return redirect(url_for('Index'))

@app.route('/edit/<string:id>')
def get_contact(id):
	cur = mysql.connection.cursor()
	cur.execute('SELECT * FROM datos_estudio WHERE id = {0}'.format(id))
	data = cur.fetchall()
	return render_template('edit-contact.html', contact = data[0])
@app.route('/ver/<id>')
def ver_contact(id):
	cur = mysql.connection.cursor()
	cur.execute('SELECT * FROM datos_estudio WHERE id = {0}'.format(id))
	data = cur.fetchall()
	return render_template('ver_datos.html', contact = data[0])  
@app.route('/update/<id>', methods=['POST'])
def updata_contact(id):
	if request.method == 'POST':
		nombre = request.form['nombre']
		fecha_na = request.form['fecha_na']
		sexo = request.form['sexo']
		edad = request.form['edad']
		peso = request.form['peso']
		altura = request.form['altura']
		tel = request.form['tel']
		cel = request.form['cel']
		obra_s = request.form['obra_s']
		numero_a = request.form['numero_a']
		tipo_p = request.form['tipo_p']
		capacidad_e = request.form['capacidad_e']
		fecha_e = request.form['fecha_e']
		medico_o = request.form['medico_o']
		medico_d = request.form['medico_d']
		protocolo = request.form['protocolo']
		observaciones = request.form['observaciones']
		motivo_e = request.form['motivo_e']
		antecedentes = request.form['antecedentes']
		factores_r = request.form['factores_r']
		ecg = request.form['ecg']
		eco = request.form['eco']
		septum = request.form['septum']
		pared_p = request.form['pared_p']
		dfd = request.form['dfd']
		dfs = request.form['dfs']
		imvi = request.form['imvi']
		habitual = request.form['habitual']
		terapia = request.form['terapia']
		minutos = request.form['minutos']
		carga = request.form['carga']
		prueba_b = request.form['prueba_b']
		fcmp = request.form['fcmp']
		fcmp_porcentaje = request.form['fcmp_porcentaje']
		vfcb = request.form['vfcb']
		vfcmax = request.form['vfcmax']
		rcd = request.form['rcd']
		alt_ecg = request.form['alt_ecg']
		isquemia = request.form['isquemia']
		test_ad = request.form['test_ad']
		motivo = request.form['motivo']
		tiempo_i = request.form['tiempo_i']
		diagnostico = request.form['diagnostico']
		conclusiones = request.form['conclusiones']
		cur = mysql.connection.cursor()
		cur.execute(""" 
			UPDATE datos_estudio
			SET nombre=%s, fecha_na=%s, sexo=%s, edad=%s, peso=%s, altura=%s, tel=%s, cel=%s, obra_s=%s, numero_a=%s,
                tipo_p=%s, capacidad_e=%s, fecha_e=%s, medico_o=%s, medico_d=%s, protocolo=%s, observaciones=%s,
                motivo_e=%s, antecedentes=%s, factores_r=%s, ecg=%s, eco=%s, septum=%s, pared_p=%s, dfd=%s,dfs=%s, imvi=%s,
                habitual=%s, terapia=%s, minutos=%s, carga=%s, prueba_b=%s, fcmp=%s, fcmp_porcentaje=%s, vfcb=%s,
                vfcmax=%s, rcd=%s, alt_ecg=%s, isquemia=%s, test_ad=%s, motivo=%s, tiempo_i=%s, diagnostico=%s,
                conclusiones=%s
			WHERE id = %s
		""", (nombre, fecha_na, sexo,edad, peso, altura, tel, cel, obra_s, numero_a, tipo_p, capacidad_e, fecha_e,
            medico_o, medico_d, protocolo, observaciones, motivo_e, antecedentes, factores_r, ecg, eco, septum,
            pared_p, dfd,dfs, imvi, habitual, terapia, minutos, carga, prueba_b, fcmp, fcmp_porcentaje, vfcb, vfcmax,
            rcd, alt_ecg, isquemia, test_ad, motivo, tiempo_i, diagnostico, conclusiones, id))
		mysql.connection.commit()
		flash('Se ah actualizado correctamente')
		return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
	cur = mysql.connection.cursor()
	cur.execute('DELETE FROM datos_estudio WHERE id = {0}'.format(id))
	mysql.connection.commit()
	flash('Fue eliminado correctamente')
	return redirect(url_for('Index'))
@app.route('/extraer_datos')
def extraer_datos():
	return render_template('extraer_datos.html')

@app.route('/upload', methods=['POST'])
def upload():

    
	filew = request.files['filess']
	file = filew.filename
	reader = PdfReader(filew)
	number_of_pages = len(reader.pages)
	texto = ""
	line = ""

	for page_num in range(number_of_pages):
		page = reader.pages[page_num]
		texto += page.extract_text()

	texto_unido = " ".join(line.strip() for line in texto.splitlines())
	lines = texto.split('\n')

	texto_a_buscar = "Estudio de Eco Estrés"

	# Usar el operador 'in' para verificar si el texto está en el párrafo
	existe = texto_a_buscar in texto_unido

	if existe:
		    #nombre y apellido
            if 'Apellido y nombre:' in texto_unido:
                nombre=texto_unido.split('Apellido y nombre:')[1].strip()
                posicion_nomb = nombre.find("Fecha de Nacimiento")
                nombre = nombre[:posicion_nomb]
                nomb=nombre
            else:
            	nomb="None"
            #fecha nacieminento
            if 'Fecha de Nacimiento:' in texto_unido:
                fecha_naci=texto_unido.split('Fecha de Nacimiento:')[1].strip()
                posicion_na = fecha_naci.find("Sexo:")
                fecha_naci = fecha_naci[:posicion_na]
                fecha_na =fecha_naci
            else:
            	fecha_na ="None"
            #sexo
            if 'Sexo:' in texto_unido:
                sexo=texto_unido.split('Sexo:')[1].strip()
                posicion_sexo = sexo.find("Edad:")
                sexo = sexo[:posicion_sexo]
                sex =sexo
            else:
            	sex ="None"
            #edad
            if 'Edad:' in texto_unido:
                edad=texto_unido.split('Edad:')[1].strip()
                posicion_edad = edad.find("Peso:")
                edad = edad[:posicion_edad]
                eda =edad
            else:
            	eda ="None"
            #Peso
            if 'Peso:' in texto_unido:
                peso=texto_unido.split('Peso:')[1].strip()
                posicion_peso = peso.find("Altura:")
                peso = peso[:posicion_peso]
                pes =peso
            else:
            	pes ="None"
            #altura
            if 'Altura:' in texto_unido:
                altura=texto_unido.split('Altura:')[1].strip()
                posicion_altura = altura.find("Teléfono:")
                posicion_altura2 = altura.find("Obra Social:")
                if posicion_altura != -1:
                    altura=altura[:posicion_altura]
                elif posicion_altura2 != -1:
                    altura=altura[:posicion_altura2]
                alt =altura
            else:
            	alt ="None"
            #Teléfono
            if 'Teléfono:' in texto_unido:
                telefon=texto_unido.split('Teléfono:')[1].strip()
                posicion_tel = telefon.find("Celular:")
                telefon = telefon[:posicion_tel]
                tel =telefon
            else:
            	tel ="None"
            #Celular
            if 'Celular:' in texto_unido:
                celular=texto_unido.split('Celular:')[1].strip()
                posicion_cel = celular.find("Obra Social:")
                celular = celular[:posicion_cel]
                cel =celular
            else:
            	cel ="None"
            #Obra Social
            if 'Obra Social:' in texto_unido:
                obra_soc=texto_unido.split('Obra Social:')[1].strip()
                posicion_obra = obra_soc.find("Número de Afiliado:")
                posicion_dats = obra_soc.find("Datos del estudio")
                if posicion_altura != -1:
                    obra_soc=obra_soc[:posicion_obra]
                elif posicion_altura2 != -1:
                    obra_soc=obra_soc[:posicion_dats]
                obra_s =obra_soc
            else:
            	obra_s ="None"
            #Número de Afiliado
            if 'Número de Afiliado:' in texto_unido:
                numero_afi=texto_unido.split('Número de Afiliado:')[1].strip()
                posicion_afi = numero_afi.find("Tipo de Paciente")
                numero_afi = numero_afi[:posicion_afi]
                numero_a=numero_afi
            else:
            	numero_a="None"
            #Tipo de Paciente
            if 'Tipo de Paciente:' in texto_unido:
                tipo_pac =texto_unido.split('Tipo de Paciente:')[1].strip()
                posicion_pac = tipo_pac.find("Capacidad de Realizar Ejercicio:")
                tipo_pac = tipo_pac[:posicion_pac]
                tipo_p =tipo_pac
            else:
            	tipo_p ="None"
            #Capacidad de Realizar Ejercicio
            if 'Capacidad de Realizar Ejercicio:' in texto_unido:
                capacidad =texto_unido.split('Capacidad de Realizar Ejercicio:')[1].strip()
                posicion_capacidad = capacidad.find("Datos del estudio")
                capacidad = capacidad[:posicion_capacidad]
                ejerc =capacidad
            else:
            	ejerc ="None"
            #fecha de estudio
            if 'Fecha:' in texto_unido:
                fecha =texto_unido.split('Fecha:')[1].strip()
                posicion_fecha = fecha.find("Médico Operador")
                fecha = fecha[:posicion_fecha]
                fecha_es =fecha
            else:
            	fecha_es ="None"
            #Médico Operador
            if 'Médico Operador:' in texto_unido:
                med_ope =texto_unido.split('Médico Operador:')[1].strip()
                posicion_med = med_ope.find(" Médico Derivador:")
                posicion_de = med_ope.find("Interrogatorio previo")
                if posicion_med != -1:
                    med_ope=med_ope[:posicion_med]
                elif posicion_de != -1:
                    med_ope=med_ope[:posicion_de]
                med_o =med_ope
            else:
            	med_o ="None"
            #Médico Derivador
            if 'Médico Derivador:' in texto_unido:
                med_deriva =texto_unido.split('Médico Derivador:')[1].strip()
                posicion_deriva = med_deriva.find("Protocolo")
                med_deriva=med_deriva[:posicion_deriva]
                med_d =med_deriva
            else:
            	med_d ="None"
            #Protocolo
            if 'Protocolo:' in texto_unido:
                protocolo_d =texto_unido.split('Protocolo:')[1].strip()
                posicion_protoc = protocolo_d.find("Observaciones")
                protocolo_d=protocolo_d[:posicion_protoc]
                protocolo =protocolo_d
            else:
            	protocolo ="None"
            #Observaciones
            if 'Observaciones:' in texto_unido:
                observ =texto_unido.split('Observaciones:')[1].strip()
                posicion_observ = observ.find("Interrogatorio previo")
                observ=observ[:posicion_observ]
                observaciones =observ
            else:
            	observaciones ="None"
            #Motivo del Estudio:
            if 'Motivo del Estudio:' in texto_unido:
                motivo_es =texto_unido.split('Motivo del Estudio:')[1].strip()
                posicion_motivo = motivo_es.find("Antecedentes:")
                motivo_es=motivo_es[:posicion_motivo]
                motivo =motivo_es
            else:
            	motivo ="None"
            #Antecedentes
            if 'Antecedentes:' in texto_unido:
                antecen =texto_unido.split('Antecedentes:')[1].strip()
                posicion_antecen = antecen.find("Factores de Riesgo:")
                posicion_antecen2 = antecen.find("Medicación Habitual:")
                if posicion_antecen != -1:
                    antecen=antecen[:posicion_antecen]
                else:
                    antecen=antecen[:posicion_antecen2]
                antecedentes =antecen
            else:
            	antecedentes ="None"
            #Factores de Riesgo
            if 'Factores de Riesgo:' in texto_unido:
                factores_riesgo =texto_unido.split('Factores de Riesgo:')[1].strip()
                posicion_riesgo = factores_riesgo.find("ECG Reposo:")
                factores_riesgo=factores_riesgo[:posicion_riesgo]
                fac_riesgo =factores_riesgo
            else:
            	fac_riesgo ="None"
            #ECG Reposo:
            if 'ECG Reposo:' in texto_unido:
                ECG_reposo =texto_unido.split('ECG Reposo:')[1].strip()
                posicion_ECG = ECG_reposo.find("ECO Reposo:")
                ECG_reposo=ECG_reposo[:posicion_ECG]
                ECG =ECG_reposo
            else:
            	ECG ="None"
            #ECG Reposo:
            if 'ECO Reposo:' in texto_unido:
                ECO_reposo =texto_unido.split('ECO Reposo:')[1].strip()
                posicion_ECO = ECO_reposo.find("Septum:")
                ECO_reposo=ECO_reposo[:posicion_ECO]
                ECO =ECO_reposo
            else:
            	ECO ="None"
            #Septum:
            if 'Septum:' in texto_unido:
                Septum_d =texto_unido.split('Septum:')[1].strip()
                posicion_Septum = Septum_d.find("Pared posterior:")
                Septum_d=Septum_d[:posicion_Septum]
                Septum =Septum_d
            else:
            	Septum ="None"
            #Pared posterior
            if 'Pared posterior:' in texto_unido:
                pared_pos =texto_unido.split('Pared posterior:')[1].strip()
                posicion_pared = pared_pos.find("DFD:")
                pared_pos=pared_pos[:posicion_pared]
                Pared_posterior =pared_pos
            else:
            	Pared_posterior ="None"
            #DFD
            if 'DFD:' in texto_unido:
                DFD_d =texto_unido.split('DFD:')[1].strip()
                posicion_DFD = DFD_d.find("DFS:")
                DFD_d=DFD_d[:posicion_DFD]
                DFD =DFD_d
            else:
            	DFD ="None"
            #DFS
            if 'DFS:' in texto_unido:
                DFS_d =texto_unido.split('DFS:')[1].strip()
                posicion_DFS = DFS_d.find("IMVI:")
                DFS_d=DFS_d[:posicion_DFS]
                DFS =DFS_d
            else:
            	DFS ="None"
            #IMVI
            if 'IMVI:' in texto_unido:
                IMVI_d =texto_unido.split('IMVI:')[1].strip()
                posicion_IMVI = IMVI_d.find("Medicación Habitual:")
                IMVI_d=IMVI_d[:posicion_IMVI]
                IMVI =IMVI_d
            else:
            	IMVI ="None"
            #Medicación Habitual
            if 'Medicación Habitual:' in texto_unido:
                habitual_d =texto_unido.split('Medicación Habitual:')[1].strip()
                posicion_habitual = habitual_d.find("Terapia antisquémica:")
                posicion_habitual2 = habitual_d.find("Minutos ejercitados:")
                if posicion_habitual != -1:
                	habitual_d=habitual_d[:posicion_habitual]
                else:
                	habitual_d=habitual_d[:posicion_habitual2]
                habitual =habitual_d
            else:
            	habitual ="None"
            #Terapia antisquémica
            if 'Terapia antisquémica:' in texto_unido:
                terapia =texto_unido.split('Terapia antisquémica:')[1].strip()
                posicion_terapia = terapia.find("Minutos ejercitados:")
                terapia=terapia[:posicion_terapia]
                Terapia_anti =terapia
            else:
            	Terapia_anti ="None"
            #Minutos ejercitados:
            if 'Minutos ejercitados:' in texto_unido:
                minuto =texto_unido.split('Minutos ejercitados:')[1].strip()
                posicion_minuto = minuto.find("Carga máxima:")
                minuto=minuto[:posicion_minuto]
                minuto =minuto
            else:
            	minuto ="None"
            #Carga máxima:
            if 'Carga máxima:' in texto_unido:
                carga_d =texto_unido.split('Carga máxima:')[1].strip()
                posicion_carga = carga_d.find("Prueba bajo medicación:")
                posicion_carga2 = carga_d.find("% de FCMP alcanzada:")
                if posicion_carga != -1:
                	carga_d=carga_d[:posicion_carga]
                else:
                	carga_d=carga_d[:posicion_carga2]
                carga =carga_d
            else:
            	carga ="None"
            #Prueba bajo medicación:
            if 'Prueba bajo medicación:' in texto_unido:
                prueba_b =texto_unido.split('Prueba bajo medicación:')[1].strip()
                posicion_prueba = prueba_b.find("FCMP:")
                prueba_b=prueba_b[:posicion_prueba]
                Prueba_bajo =prueba_b
            else:
            	Prueba_bajo ="None"
            #FCMP:
            if 'FCMP:' in texto_unido:
                FCMP_d =texto_unido.split('FCMP:')[1].strip()
                posicion_FCMP = FCMP_d.find("% de FCMP alcanzada:")
                FCMP_d=FCMP_d[:posicion_FCMP]
                FCMP =FCMP_d
            else:
            	FCMP ="None"
            #% de FCMP alcanzada:
            if '% de FCMP alcanzada:' in texto_unido:
                porcentaje =texto_unido.split('% de FCMP alcanzada:')[1].strip()
                posicion_porcentaje = porcentaje.find("Reserva Coronaria :")
                porcentaje=porcentaje[:posicion_porcentaje]
                FCMP_porcentaje =porcentaje
            else:
            	FCMP_porcentaje ="None"
            #VFCB
            if 'VFCB:' in texto_unido:
                VFCB_d =texto_unido.split('VFCB:')[1].strip()
                posicion_VFCB = VFCB_d.find("VFCMax:")
                VFCB_d=VFCB_d[:posicion_VFCB]
                VFCB =VFCB_d
            else:
            	VFCB ="None"
            #VFCMax
            if 'VFCMax:' in texto_unido:
                VFCMax_d =texto_unido.split('VFCMax:')[1].strip()
                posicion_VFCMax = VFCMax_d.find("RCD:")
                VFCMax_d=VFCMax_d[:posicion_VFCMax]
                VFCMax =VFCMax_d
            else:
            	VFCMax ="None"
            #RCD
            if 'RCD:' in texto_unido:
                RCD_b =texto_unido.split('RCD:')[1].strip()
                posicion_RCD = RCD_b.find("Alteraciones en el ECG:")
                RCD_b=RCD_b[:posicion_RCD]
                RCD =RCD_b
            else:
            	RCD ="None"
            #Alteraciones en el ECG
            if 'Alteraciones en el ECG:' in texto_unido:
                Alt_ECG_d =texto_unido.split('Alteraciones en el ECG:')[1].strip()
                posicion_Alt_ECG = Alt_ECG_d.find("Remisión de isquemia:")
                Alt_ECG_d=Alt_ECG_d[:posicion_Alt_ECG]
                Alt_ECG =Alt_ECG_d
            else:
            	Alt_ECG ="None"
            #Remisión de isquemia:
            if 'Remisión de isquemia:' in texto_unido:
                isquemia_d =texto_unido.split('Remisión de isquemia:')[1].strip()
                posicion_isquemia = isquemia_d.find("Test detenido por efectos adversos :")
                isquemia_d=isquemia_d[:posicion_isquemia]
                isquemia =isquemia_d
            else:
            	isquemia ="None"
            #Test detenido por efectos adversos :
            if 'Test detenido por efectos adversos :' in texto_unido:
                test_ad_d =texto_unido.split('Test detenido por efectos adversos :')[1].strip()
                posicion_test_ad = test_ad_d.find("Motivo:")
                test_ad_d=test_ad_d[:posicion_test_ad]
                test_ad =test_ad_d
            else:
            	test_ad ="None"
            #Motivo
            if 'Motivo:' in texto_unido:
                motivo_test_d =texto_unido.split('Motivo:')[1].strip()
                posicion_motivo_test = motivo_test_d.find("Tiempo de inicio:")
                motivo_test_d=motivo_test_d[:posicion_motivo_test]
                motivo_test =motivo_test_d
            else:
            	motivo_test ="None"
            #Tiempo de inicio
            if 'Tiempo de inicio:' in texto_unido:
                Tiempo_inicio_d =texto_unido.split('Tiempo de inicio:')[1].strip()
                posicion_Tiempo_inicio = Tiempo_inicio_d.find("Diagnóstico :")
                Tiempo_inicio_d=Tiempo_inicio_d[:posicion_Tiempo_inicio]
                Tiempo_inicio =Tiempo_inicio_d
            else:
            	Tiempo_inicio ="None"
            if 'Diagnóstico :' in texto_unido:
                capacidad_dig=texto_unido.split('Diagnóstico :')[1].strip()
                posicion_dig = capacidad_dig.find("Conclusiones :")
                capacidad_dig = capacidad_dig[:posicion_dig]
                diagnostico = capacidad_dig
            else:
                diagnostico = "None"

            if 'Conclusiones :' in texto_unido:
                capacidad_concl=texto_unido.split('Conclusiones :')[1].strip()
                posicion_concl = capacidad_concl.find("Etapa FC PA")
                capacidad_concl = capacidad_concl[:posicion_concl]
                conclusiones=capacidad_concl

            else:
            	conclusiones = "None"
            fecha_nacimie = parser.parse(fecha_na, dayfirst=True)
            fecha_est = parser.parse(fecha_es, dayfirst=True)
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO datos_estudio (nombre, fecha_na, sexo, edad, peso, altura, tel, cel, obra_s, numero_a, tipo_p, capacidad_e, fecha_e, medico_o, medico_d, protocolo, observaciones, motivo_e,antecedentes, factores_r, ecg, eco, septum, pared_p, dfd, dfs, imvi, habitual, terapia, minutos, carga, prueba_b, fcmp, fcmp_porcentaje, vfcb, vfcmax, rcd, alt_ecg, isquemia,test_ad,motivo,tiempo_i,diagnostico,conclusiones,file) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (nomb, fecha_nacimie, sex, eda, pes, alt, tel, cel, obra_s, numero_a, tipo_p, ejerc, fecha_est, med_o, med_d, protocolo, observaciones, motivo, antecedentes, fac_riesgo,ECG,ECO,Septum,Pared_posterior,DFD,DFS,IMVI,habitual,Terapia_anti,minuto,carga,Prueba_bajo,FCMP,FCMP_porcentaje,VFCB,VFCMax,RCD,Alt_ECG,isquemia,test_ad,motivo_test,Tiempo_inicio,diagnostico,conclusiones,file))
            mysql.connection.commit()

            flash('Se subido el archivo correctamente')
            return redirect(url_for('Index'))
	else:
            flash('No se subiedo este archivo porque no tiene los datos esfecivios')
            return redirect(url_for('Index'))

	
    

	print(file)
	
	return 'hola'
if __name__ == '__main__':
	app.run(debug=True, port=5000)