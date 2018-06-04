from flask import render_template, flash, redirect, url_for, request, current_app
from app.urea.forms import CaseForm,RawmaterialForm,TransportForm,ProcessmaterialForm,WasteForm
from app.models import User,Case,Rawmaterial,Transport,Processmaterial,Waste,Caserawmaterial,Casetransport,Caseprocessmaterial,Casewaste
from app import db
from werkzeug.urls import url_parse
from app.urea import bp
from flask_login import current_user,login_required

@bp.route("/admin",methods=["GET","POST"])
@login_required
def admin():
	rawmaterialform=RawmaterialForm()
	transportform=TransportForm()
	processmaterialform=ProcessmaterialForm()
	wasteform=WasteForm()
	
	if rawmaterialform.rawmaterialsubmit.data:
		form=rawmaterialform
		if form.id.data==0:
			exist=Rawmaterial.query.filter_by(name=form.name.data).first()
			if exist is not None:
				flash('原料选项<{}>已存在，添加失败.'.format(form.name.data))
			else:
				rawmaterial=Rawmaterial(name=form.name.data, unit=form.unit.data, default=form.default.data)
				db.session.add(rawmaterial)
				db.session.commit()
				flash('原料选项<{}>添加成功.'.format(form.name.data))
		else:
			exist=Rawmaterial.query.filter(Rawmaterial.name==form.name.data,Rawmaterial.id!=form.id.data).first()
			if exist is not None:
				flash('原料选项<{}>已存在，修改失败.'.format(form.name.data))
			else:
				rawmaterial=Rawmaterial.query.filter_by(id=form.id.data).first()
				if rawmaterial is None:
					flash('修改失败，找不到指定的原料选项.')
				else:
					rawmaterial.name=form.name.data
					rawmaterial.unit=form.unit.data
					rawmaterial.default=form.default.data
					db.session.commit()
					flash('原料选项<{}>编辑成功.'.format(form.name.data))
	
	transportform.rawmaterial.choices=[(item.id,item.name) for item in Rawmaterial.query.all()]
 
	if transportform.transportsubmit.data:
		form=transportform
		if form.id.data==0:
			rawmaterial=Rawmaterial.query.filter_by(id=form.rawmaterial.data).first()
			if rawmaterial is None:
				flash('所选原料不存在，添加失败.')
			else:
				exist=Transport.query.filter_by(method=form.method.data,rawmaterial=rawmaterial).first()
				if exist is not None:
					flash('原料<{}>的运输方式选项<{}>已存在，添加失败.'.format(rawmaterial.name,form.method.data))
				else:
					transport=Transport(method=form.method.data, unit=form.unit.data,default=form.default.data, rawmaterial=rawmaterial)
					db.session.add(transport)
					db.session.commit()
					flash('添加成功.')
		else:
			transport=Transport.query.filter_by(id=form.id.data).first()
			if transport is None:
				flash('修改失败，找不到指定的运输方式选项.')
			else:
				exist=Transport.query.filter(Transport.method==form.method.data,Transport.rawmaterial==transport.rawmaterial,Transport.id!=form.id.data).first()
				if exist is not None:
					flash('原料<{}>的运输方式选项<{}>已存在，修改失败.'.format(transport.rawmaterial.name,form.method.data))
				else:
					transport.method=form.method.data
					transport.unit=form.unit.data
					transport.default=form.default.data
					db.session.commit()
					flash('编辑成功.')
	
	if processmaterialform.processmaterialsubmit.data:
		form=processmaterialform
		if form.id.data==0:
			exist=Processmaterial.query.filter_by(name=form.name.data).first()
			if exist is not None:
				flash('生产过程消耗材料选项<{}>已存在，添加失败.'.format(form.name.data))
			else:
				processmaterial=Processmaterial(name=form.name.data, unit=form.unit.data, default=form.default.data)
				db.session.add(processmaterial)
				db.session.commit()
				flash('生产过程消耗材料选项<{}>添加成功.'.format(form.name.data))
		else:
			exist=Processmaterial.query.filter(Processmaterial.name==form.name.data,Processmaterial.id!=form.id.data).first()
			if exist is not None:
				flash('生产过程消耗材料选项<{}>已存在，修改失败.'.format(form.name.data))
			else:
				processmaterial=Processmaterial.query.filter_by(id=form.id.data).first()
				if processmaterial is None:
					flash('修改失败，找不到指定的材料选项.')
				else:
					processmaterial.name=form.name.data
					processmaterial.unit=form.unit.data
					processmaterial.default=form.default.data
					db.session.commit()
					flash('生产过程消耗材料选项<{}>编辑成功.'.format(form.name.data))
	
	if wasteform.wastesubmit.data:
		form=wasteform
		if form.id.data==0:
			exist=Waste.query.filter_by(name=form.name.data).first()
			if exist is not None:
				flash('废弃物处理选项<{}>已存在，添加失败.'.format(form.name.data))
			else:
				waste=Waste(name=form.name.data, unit=form.unit.data, default=form.default.data)
				db.session.add(waste)
				db.session.commit()
				flash('废弃物处理选项<{}>添加成功.'.format(form.name.data))
		else:
			exist=Waste.query.filter(Waste.name==form.name.data,Waste.id!=form.id.data).first()
			if exist is not None:
				flash('废弃物处理选项<{}>已存在，修改失败.'.format(form.name.data))
			else:
				waste=Waste.query.filter_by(id=form.id.data).first()
				if waste is None:
					flash('修改失败，找不到指定的废弃物处理选项.')
				else:
					waste.name=form.name.data
					waste.unit=form.unit.data
					waste.default=form.default.data
					db.session.commit()
					flash('废弃物处理选项<{}>编辑成功.'.format(form.name.data))
	

	rawmaterials=Rawmaterial.query.order_by(Rawmaterial.name).all()
	transports=Transport.query.join(Transport.rawmaterial).order_by(Rawmaterial.name,Transport.method).all()
	processmaterials=Processmaterial.query.order_by(Processmaterial.name).all()
	wastes=Waste.query.order_by(Waste.name).all()

	return render_template('urea/admin.html',title='过程选项管理',rawmaterials=rawmaterials,transports=transports,processmaterials=processmaterials,wastes=wastes,rawmaterialform=rawmaterialform,transportform=transportform,processmaterialform=processmaterialform,wasteform=wasteform)

@bp.route("/delrawmaterial",methods=['POST'])
def delrawmaterial():
	rawmaterial_id=request.form['id']
	rawmaterial=Rawmaterial.query.filter_by(id=rawmaterial_id).first()
	if rawmaterial is None:
		return 'fail'
	else:
		for item in rawmaterial.transports:
			db.session.delete(item)
		db.session.delete(rawmaterial)
		db.session.commit()
		rawmaterials=Rawmaterial.query.order_by(Rawmaterial.name).all()
		transports=Transport.query.join(Transport.rawmaterial).order_by(Rawmaterial.name,Transport.method).all()
		transportform=TransportForm()
		transportform.rawmaterial.choices=[(item.id,item.name) for item in Rawmaterial.query.all()]
		return render_template('urea/_randt.html',rawmaterials=rawmaterials,transports=transports,transportform=transportform)

@bp.route("/deltransport",methods=['POST'])
def deltransport():
	transport_id=request.form['id']
	transport=Transport.query.filter_by(id=transport_id).first()
	if transport is None:
		return 'fail'
	else:
		db.session.delete(transport)
		db.session.commit()
		transports=Transport.query.join(Transport.rawmaterial).order_by(Rawmaterial.name,Transport.method).all()
		return render_template('urea/_transports.html',transports=transports)

@bp.route("/delprocessmaterial",methods=["POST"])
def delprocessmaterial():
	processmaterial_id=request.form['id']
	processmaterial=Processmaterial.query.filter_by(id=processmaterial_id).first()
	if processmaterial is None:
		return 'fail'
	else:
		db.session.delete(processmaterial)
		db.session.commit()
		processmaterials=Processmaterial.query.order_by(Processmaterial.name).all()
		return render_template('urea/_processmaterials.html',processmaterials=processmaterials)

@bp.route("/delwaste",methods=["POST"])
def delwaste():
	waste_id=request.form['id']
	waste=Waste.query.filter_by(id=waste_id).first()
	if waste is None:
		return 'fail'
	else:
		db.session.delete(waste)
		db.session.commit()
		wastes=Waste.query.order_by(Waste.name).all()
		return render_template('urea/_wastes.html',wastes=wastes)

@bp.route("/cases",methods=["GET","POST"])
@login_required
def cases():
	form=CaseForm()
	if form.submit.data:
		existcase=Case.query.filter_by(name=form.name.data,user=current_user).first()
		if existcase is not None:
			flash('案例名称<{}>已存在，添加失败。'.format(form.name.data))
		else:
			case=Case(name=form.name.data,user=current_user,quantitytype='single')
			db.session.add(case)
			db.session.commit()
			flash('案例<{}>添加成功.'.format(form.name.data))
	cases=Case.query.filter_by(user=current_user).order_by(Case.name).all()
	return render_template('urea/cases.html',title='案例管理',cases=cases,form=form)

@bp.route("/case/<id>",methods=["GET","POST"])
@login_required
def case(id):
	case=Case.query.filter_by(id=id,user=current_user).first()
	if case is None:
		flash('您的案例列表中不存在该案例')
		return redirect(url_for('urea.cases'))
	else:
		if request.method=='POST':
			value=0
			tran_value=0
			raws=Rawmaterial.query.all()
			for raw in raws:
				uec=request.form.get("raw-{}-uec".format(raw.id))
				uq=request.form.get("raw-{}-uq".format(raw.id))
				if uec is not None and uq is not None:	
					uec=float(uec)
					uq=float(uq)
					rawcase=Caserawmaterial.query.filter_by(case=case,rawmaterial=raw).first()
					if rawcase is None:
						rawcase=Caserawmaterial(case=case,\
							rawmaterial=raw,\
							unitquantity=uq,\
							unitenergyconsumption=uec)
						db.session.add(rawcase)
					else:
						rawcase.unitquantity=uq
						rawcase.unitenergyconsumption=uec
					value=value+uec*uq
				for tran in raw.transports:
					tran_uec=request.form.get("tran-{}-uec".format(tran.id))
					tran_uq=request.form.get("tran-{}-uq".format(tran.id))
					if tran_uec is not None and tran_uq is not None:
						tran_uec=float(tran_uec)
						tran_uq=float(tran_uq)
						trancase=Casetransport.query.filter_by(case=case,transport=tran).first()
						if trancase is None:
							trancase=Casetransport(case=case,\
								transport=tran,\
								unitquantity=tran_uq,\
								unitenergyconsumption=tran_uec)
							db.session.add(trancase)
						else:
							trancase.unitquantity=tran_uq
							trancase.unitenergyconsumption=tran_uec
						tran_value=tran_value+tran_uec*tran_uq*uq
			pros=Processmaterial.query.all()
			for pro in pros:
				uec=request.form.get("pro-{}-uec".format(pro.id))
				uq=request.form.get("pro-{}-uq".format(pro.id))
				if uec is not None and uq is not None:
					uec=float(uec)
					uq=float(uq)
					procase=Caseprocessmaterial.query.filter_by(case=case,processmaterial=pro).first()
					if procase is None:
						procase=Caseprocessmaterial(case=case,\
							processmaterial=pro,\
							unitquantity=uq,
							unitenergyconsumption=uec)
						db.session.add(procase)
					else:
						procase.unitquantity=uq
						procase.unitenergyconsumption=uec
					value=value+uec*uq
			wastes=Waste.query.all()
			for waste in wastes:
				uec=request.form.get("waste-{}-uec".format(waste.id))
				uq=request.form.get("waste-{}-uq".format(waste.id))
				if uec is not None and uq is not None:
					uec=float(uec)
					uq=float(uq)
					wastecase=Casewaste.query.filter_by(case=case,waste=waste).first()
					if wastecase is None:
						wastecase=Casewaste(case=case,\
							waste=waste,\
							unitquantity=uq,\
							unitenergyconsumption=uec)
						db.session.add(wastecase)
					else:
						wastecase.unitquantity=uq
						wastecase.unitenergyconsumption=uec
					value=value+uec*uq
			case.quantitytype=request.form['quantitytype']
			case.productquantity=float(request.form['urea'])
			if case.quantitytype=="single":
				case.efficiency=value+tran_value
				case.energyconsumption=(value+tran_value)*case.productquantity
			else:
				case.energyconsumption=value+tran_value
				if case.productquantity==0:
					case.efficiency=0
				else:
					case.efficiency=(value+tran_value)/case.productquantity
			db.session.commit()
			return redirect(url_for('urea.cases'))
		rawcases=[]
		raws=Rawmaterial.query.order_by(Rawmaterial.name).all()
		for raw in raws:
			exist=False
			for item in case.rawmaterials:
				if item.rawmaterial==raw:
					rawcases.append(item)
					exist=True
			if not exist:	
				rawcase=Caserawmaterial(case=case,\
					rawmaterial=raw,\
					unitenergyconsumption=raw.default,\
					unitquantity=0)
				rawcases.append(rawcase)
		transcases=[]
		transports=Transport.query.order_by(Transport.method).all()
		for transport in transports:
			exist=False
			for item in case.transports:
				if item.transport==transport:
					transcases.append(item)
					exist=True
			if not exist:
				transcase=Casetransport(case=case,\
					transport=transport,\
					unitenergyconsumption=transport.default,\
					unitquantity=0)
				transcases.append(transcase)
		procases=[]
		pros=Processmaterial.query.order_by(Processmaterial.name).all()
		for pro in pros:
			exist=False
			for item in case.processmaterials:
				if item.processmaterial==pro:
					procases.append(item)
					exist=True
			if not exist:
				procase=Caseprocessmaterial(case=case,\
					processmaterial=pro,\
					unitenergyconsumption=pro.default,\
					unitquantity=0)
				procases.append(procase)
		wastecases=[]
		wastes=Waste.query.order_by(Waste.name).all()
		for waste in wastes:
			exist=False
			for item in case.wastes:
				if item.waste==waste:
					wastecases.append(item)
					exist=True
			if not exist:
				wastecase=Casewaste(case=case,\
					waste=waste,\
					unitenergyconsumption=waste.default,\
					unitquantity=0)
				wastecases.append(wastecase)
		return render_template('urea/case.html',case=case,rawcases=rawcases,transcases=transcases,procases=procases,wastecases=wastecases)

@bp.route("/delcase",methods=["POST"])
def delcase():
	case_id=request.form['id']
	case=Case.query.filter_by(id=case_id,user=current_user).first()
	if case is None:
		return 'fail'
	else:
		db.session.delete(case)
		db.session.commit()
		cases=Case.query.filter_by(user=current_user).order_by(Case.name).all()
		return render_template('urea/_cases.html',cases=cases)
