$.fn.addrawmaterial=function(){
	$('#editRawmaterialModal').find('#id').val('0');
	$('#editRawmaterialModal').find('#name').val('');
	$('#editRawmaterialModal').find('#unit').val('');
	$('#editRawmaterialModal').find('#default').val('');
	$('#editRawmaterialModal').find('#rawmaterialsubmit').val('添加');
	$('#editRawmaterialModal').find('#name').removeAttr('readonly');
	$('#editRawmaterialModal').find('.modal-title').text('添加原料选项');
}
	
$.fn.editrawmaterial=function(){
	var row=$(this).parent().parent();
	var id=row.find('#rawmaterialid').text();
	var name=row.find('#rawmaterialname').text();
	var unit=row.find('#rawmaterialunit').text();
	var defaultvalue=row.find('#rawmaterialdefault').text();
	$('#editRawmaterialModal').find('#id').val(id);
	$('#editRawmaterialModal').find('#name').val(name);
	$('#editRawmaterialModal').find('#unit').val(unit);
	$('#editRawmaterialModal').find('#default').val(defaultvalue);
	$('#editRawmaterialModal').find('#rawmaterialsubmit').val('确定');
	$('#editRawmaterialModal').find('#name').attr('readonly','readonly');
	$('#editRawmaterialModal').find('.modal-title').text('编辑原料选项');
}

$.fn.delrawmaterial=function(){
	var row=$(this).parent().parent();
	var id=row.find('#rawmaterialid').text();
	var name=row.find('#rawmaterialname').text();
	$('#delModal').find('#del-id').text(id);
	$('#delModal').find('#del-name').text(name);
	$('#delModal').find('#del-action').text('delrawmaterial');
	$('#delModal').find('#del-message').text('确认删除原料选项 <'+name+'> 及其相关运输方式选项数据吗？');
}

$.fn.addtransport=function(){
	$('#editTransportModal').find('#id').val('0');
	$('#editTransportModal').find('#rawmaterial').val('-1');
	$('#editTransportModal').find('#method').val('');
	$('#editTransportModal').find('#unit').val('');
	$('#editTransportModal').find('#default').val('');
	$('#editTransportModal').find('#transportsubmit').val('添加');
	$('#editTransportModal').find('#rawmaterial').removeAttr('disabled');
	$('#editTransportModal').find('.modal-title').text('添加运输方式选项');
}
	
$.fn.edittransport=function(){
	var row=$(this).parent().parent();
	var id=row.find('#transportid').text();
	var rawmaterialid=row.find('#rawmaterialid').text();
	var method=row.find('#transportmethod').text();
	var unit=row.find('#transportunit').text();
	var defaultvalue=row.find('#transportdefault').text();
	$('#editTransportModal').find('#id').val(id);
	$('#editTransportModal').find('#rawmaterial').val(rawmaterialid);
	$('#editTransportModal').find('#method').val(method);
	$('#editTransportModal').find('#unit').val(unit);
	$('#editTransportModal').find('#default').val(defaultvalue);
	$('#editTransportModal').find('#transportsubmit').val('确定');
	$('#editTransportModal').find('#rawmaterial').attr('disabled','true');
	$('#editTransportModal').find('.modal-title').text('编辑运输方式选项');
}

$.fn.deltransport=function(){
	var row=$(this).parent().parent();
	var id=row.find('#transportid').text();
	var name=row.find('#rawmaterial').text()+"："+row.find('#transportmethod').text();
	$('#delModal').find('#del-id').text(id);
	$('#delModal').find('#del-name').text(name);
	$('#delModal').find('#del-action').text('deltransport');
	$('#delModal').find('#del-message').text('确认删除运输方式选项 <'+name+'> 吗？');
}

$.fn.addprocessmaterial=function(){
	$('#editProcessmaterialModal').find('#id').val('0');
	$('#editProcessmaterialModal').find('#name').val('');
	$('#editProcessmaterialModal').find('#unit').val('');
	$('#editProcessmaterialModal').find('#default').val('');
	$('#editProcessmaterialModal').find('#processmaterialsubmit').val('添加');
	$('#editProcessmaterialModal').find('#name').removeAttr('readonly');
	$('#editProcessmaterialModal').find('.modal-title').text('添加生产过程消耗品选项');
}
	
$.fn.editprocessmaterial=function(){
	var row=$(this).parent().parent();
	var id=row.find('#processmaterialid').text();
	var name=row.find('#processmaterialname').text();
	var unit=row.find('#processmaterialunit').text();
	var defaultvalue=row.find('#processmaterialdefault').text();
	$('#editProcessmaterialModal').find('#id').val(id);
	$('#editProcessmaterialModal').find('#name').val(name);
	$('#editProcessmaterialModal').find('#unit').val(unit);
	$('#editProcessmaterialModal').find('#default').val(defaultvalue);
	$('#editProcessmaterialModal').find('#processmaterialsubmit').val('确定');
	$('#editProcessmaterialModal').find('#name').attr('readonly','readonly');
	$('#editProcessmaterialModal').find('.modal-title').text('编辑生产过程消耗品选项');
}

$.fn.delprocessmaterial=function(){
	var row=$(this).parent().parent();
	var id=row.find('#processmaterialid').text();
	var name=row.find('#processmaterialname').text();
	$('#delModal').find('#del-id').text(id);
	$('#delModal').find('#del-name').text(name);
	$('#delModal').find('#del-action').text('delprocessmaterial');
	$('#delModal').find('#del-message').text('确认删除生产过程消耗品选项 <'+name+'> 吗？');
}

$.fn.addwaste=function(){
	$('#editWasteModal').find('#id').val('0');
	$('#editWasteModal').find('#name').val('');
	$('#editWasteModal').find('#unit').val('');
	$('#editWasteModal').find('#default').val('');
	$('#editWasteModal').find('#wastesubmit').val('添加');
	$('#editWasteModal').find('#name').removeAttr('readonly');
	$('#editWasteModal').find('.modal-title').text('添加废弃物处理方式选项');
}
	
$.fn.editwaste=function(){
	var row=$(this).parent().parent();
	var id=row.find('#wasteid').text();
	var name=row.find('#wastename').text();
	var unit=row.find('#wasteunit').text();
	var defaultvalue=row.find('#wastedefault').text();
	$('#editWasteModal').find('#id').val(id);
	$('#editWasteModal').find('#name').val(name);
	$('#editWasteModal').find('#unit').val(unit);
	$('#editWasteModal').find('#default').val(defaultvalue);
	$('#editWasteModal').find('#wastesubmit').val('确定');
	$('#editWasteModal').find('#name').attr('readonly','readonly');
	$('#editWasteModal').find('.modal-title').text('编辑废弃物处理方式选项');
}

$.fn.delwaste=function(){
	var row=$(this).parent().parent();
	var id=row.find('#wasteid').text();
	var name=row.find('#wastename').text();
	$('#delModal').find('#del-id').text(id);
	$('#delModal').find('#del-name').text(name);
	$('#delModal').find('#del-action').text('delwaste');
	$('#delModal').find('#del-message').text('确认删除废弃物处理方式选项 <'+name+'> 吗？');
}

$(document).ready(function(){
	$('#rawmaterials').find('.add').click(function(){
		$(this).addrawmaterial();
	});
	$('#rawmaterials').find('.edit').click(function(){
		$(this).editrawmaterial();
	});
	$('#rawmaterials').find('.del').click(function(){
		$(this).delrawmaterial();
	});
	$('#transports').find('.add').click(function(){
		$(this).addtransport();
	});
	$('#transports').find('.edit').click(function(){
		$(this).edittransport();
	});
	$('#transports').find('.del').click(function(){
		$(this).deltransport();
	});
	$('#processmaterials').find('.add').click(function(){
		$(this).addprocessmaterial();
	});
	$('#processmaterials').find('.edit').click(function(){
		$(this).editprocessmaterial();
	});
	$('#processmaterials').find('.del').click(function(){
		$(this).delprocessmaterial();
	});
	$('#wastes').find('.add').click(function(){
		$(this).addwaste();
	});
	$('#wastes').find('.edit').click(function(){
		$(this).editwaste();
	});
	$('#wastes').find('.del').click(function(){
		$(this).delwaste();
	});

	$('#del-confirm').click(function(){
		$('.alert-info').attr('style','display:none;');
		var action=$('#delModal').find('#del-action').text();
		
		if(action=='delrawmaterial'){
			var rawmaterialid=$('#delModal').find('#del-id').text();
			var rawmaterialname=$('#delModal').find('#del-name').text();
			$.post(action,{
				id:rawmaterialid,
			},
			function(result){
				if(result=='fail')
				{
					$('#alert').text("删除失败！");
					$('#alert').attr('class','alert alert-warning');
					$('#alert').attr('style','');
				}
				else
				{
					$('#rawmaterials-transports').text("");
					$('#rawmaterials-transports').append(result);
					$('#alert').text("原料选项 <"+rawmaterialname+"> 已成功删除！");
					$('#alert').attr('class','alert alert-success');
					$('#alert').attr('style','');
					$('#rawmaterials').find('.add').click(function(){
						$(this).addrawmaterial();
					});
					$('#rawmaterials').find('.edit').click(function(){
						$(this).editrawmaterial();
					});
					$('#rawmaterials').find('.del').click(function(){
						$(this).delrawmaterial();
					});
					$('#transports').find('.add').click(function(){
						$(this).addtransport();
					});
					$('#transports').find('.edit').click(function(){
						$(this).edittransport();
					});
					$('#transports').find('.del').click(function(){
						$(this).deltransport();
					});
				}
			});
		} else if(action=='deltransport'){
			var transportid=$('#delModal').find('#del-id').text();
			var transportname=$('#delModal').find('#del-name').text();
			$.post(action,{
				id:transportid,
			},
			function(result){
				if(result=='fail')
				{
					$('#alert').text("删除失败！");
					$('#alert').attr('class','alert alert-warning');
					$('#alert').attr('style','');
				}
				else
				{
					$('#transports').text("");
					$('#transports').append(result);
					$('#alert').text("运输方式选项 <"+transportname+"> 已成功删除！");
					$('#alert').attr('class','alert alert-success');
					$('#alert').attr('style','');
					$('#transports').find('.add').click(function(){
						$(this).addtransport();
					});
					$('#transports').find('.edit').click(function(){
						$(this).edittransport();
					});
					$('#transports').find('.del').click(function(){
						$(this).deltransport();
					});
				}
			});
		} else if(action=='delprocessmaterial'){
			var processmaterialid=$('#delModal').find('#del-id').text();
			var processmaterialname=$('#delModal').find('#del-name').text();
			$.post(action,{
				id:processmaterialid,
			},
			function(result){
				if(result=='fail')
				{
					$('#alert').text("删除失败！");
					$('#alert').attr('class','alert alert-warning');
					$('#alert').attr('style','');
				}
				else
				{
					$('#processmaterials').text("");
					$('#processmaterials').append(result);
					$('#alert').text("生产过程消耗品选项 <"+processmaterialname+"> 已成功删除！");
					$('#alert').attr('class','alert alert-success');
					$('#alert').attr('style','');
					$('#processmaterials').find('.add').click(function(){
						$(this).addprocessmaterial();
					});
					$('#processmaterials').find('.edit').click(function(){
						$(this).editprocessmaterial();
					});
					$('#processmaterials').find('.del').click(function(){
						$(this).delprocessmaterial();
					});
				}
			});
		} else if(action=='delwaste'){
			var wasteid=$('#delModal').find('#del-id').text();
			var wastename=$('#delModal').find('#del-name').text();
			$.post(action,{
				id:wasteid,
			},
			function(result){
				if(result=='fail')
				{
					$('#alert').text("删除失败！");
					$('#alert').attr('class','alert alert-warning');
					$('#alert').attr('style','');
				}
				else
				{
					$('#wastes').text("");
					$('#wastes').append(result);
					$('#alert').text("废弃物处理方式选项 <"+wastename+"> 已成功删除！");
					$('#alert').attr('class','alert alert-success');
					$('#alert').attr('style','');
					$('#wastes').find('.add').click(function(){
						$(this).addwaste();
					});
					$('#wastes').find('.edit').click(function(){
						$(this).editwaste();
					});
					$('#wastes').find('.del').click(function(){
						$(this).delwaste();
					});
				}
			});
		}

	});
});
