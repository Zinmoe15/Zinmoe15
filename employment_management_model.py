from odoo import models, fields

class employment_management(models.Model):
	_name = "employment.management.model"
	_description = "employment.management.model.sample"

	job_type = fields.Selection([
		('odoo developer', 'ODOO Developer'),
		('dancer modern', 'Dancer Modern'),
		('actor', 'Actor'),
	], string="Job_Type", default="odoo developer", required=True)

	name = fields.Char(string="Name")
	cv_image = fields.Binary(string="CV_Image")
	position = fields.Char(string="Position")
	salary = fields.Char(string="Salary")
	bonus = fields.Char(string="Bonus")

	zinmoekyaw_app_id = fields.Many2one('zinmoekyaw.model')