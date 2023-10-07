{
	'name' : 'zinmoekyaw application',
	'description' : 'zinmoekyaw_application',
	'author' : 'Zin Moe Kyaw',

	'website' : 'www.zinmoekyaw.com.mm',
	'category' : 'Nuvo',
	'summary' : 'zinmoekyaw',
	'depends' : [
		'base_setup',
		'mail',
	],

	'data' : [
		'zinmoekyaw_view.xml',
		'mgmg_view.xml',
		'education_backgroung_view.xml',
		'employment_management_view.xml',
		'report/zinmoekyaw_report.xml',
		'security/ir.model.access.csv',
	],
	'application' : True,
}