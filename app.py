correos =["pedro.garcia.trabajo@gmail.com","m.garcia.pro@gmail.com","ana.rodriguez.dev@gmail.com","l.martinez.mkt@gmail.com","carlos.sanchez.consultor@gmail.com","elena.gomez.mx@gmail.com","r.diaz.finanzas@gmail.com","sofia.lopez.design@gmail.com","j.torres.ing@gmail.com","maria.vazquez.rrhh@gmail.com","p.castro.ventas@gmail.com","diego.morales.tech@gmail.com","claudia.reyes.pmo@gmail.com","f.jimenez.legal@gmail.com","beatriz.ortiz.arts@gmail.com","h.ruiz.ops@gmail.com","gabriel.nunez.qa@gmail.com","s.mendoza.innova@gmail.com","jorge.acosta.trade@gmail.com","lulu.herrera.adm@gmail.com"]


usuarios=[]


for correo in correos:
    usuario = correo.split('@')[0]
    usuarios.append(usuario)
    
    if len(usuario) > 5:
        print(f"Su correo es: {correo}")
        print(f"Su usuario es: {usuario}")
        print(f"Longitud: {len(usuario)}\n")
    else:
        print(f"Correo corto: {usuario}\n")