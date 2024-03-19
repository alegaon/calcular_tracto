"""
gravamen 1.5 valor fiscal + 5%(bienes)
honorarios abogados 15% (entre 6 y 16.5%)
impuesto transferencia inmyeble (iti) 1.5%
sellos 1.8%
estudio titulos % $38000 + 0.2%
certificados diligenticia 0.2%
comision inmobiliaria 1 o 3 % + iva
certificado de dominio estudio de títulos 620$
certificadod inhibiciones 1240
tasa inscriupcion :comprador 2%
tasa justicia 3% base imponible del inmuebel


"""

def costo(valor_inmueble):
    """
    refactorizar con un dict clave valor
    lista_costos = {
        'gravamen': (0.015, 0.05),
    }

    """
    lista_costos = {

        'gravamen': (0.015, 0.05),

    }

    gravamen = valor_inmueble*0.015 + valor_inmueble * 0.05
    print(f"gravamen:{gravamen}") 

    # honorarios abogados 15% (entre 6 y 16.5%)
    honorarios = valor_inmueble * 0.15
    print(f'honorarios: {honorarios}')

    # impuesto transferencia inmyeble (iti) 1.5%
    trasferencia = valor_inmueble * 
    # sellos 1.8%
    # estudio titulos % $38000 + 0.2%
    # certificados diligenticia 0.2%
    # comision inmobiliaria 1 o 3 % + iva
    # certificado de dominio estudio de títulos 620$
    # certificadod inhibiciones 1240
    # tasa inscriupcion :comprador 2%
    # tasa justicia 3% base imponible del inmuebel
