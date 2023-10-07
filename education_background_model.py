from odoo import models, fields

class education_background(models.Model):
	_name = "education.background.model"
	_description = "education.background.model.sample"

	job_type = fields.Selection([
		('odoo developer', 'ODOO Developer'),
		('dancer modern', 'Dancer Modern'),
		('actor', 'Actor'),
	], string="Job_Type", default="odoo developer", required=True)

	name = fields.Char(string="Name")
	cv_image = fields.Binary(string="CV_Image")
	education = fields.Char(string="Education")
	level = fields.Char(string="Level")
	skill = fields.Char(string="Skill")

	zinmoekyaw_app_id = fields.Many2one('zinmoekyaw.model')