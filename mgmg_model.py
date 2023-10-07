from odoo import models, fields

class mgmg(models.Model):
	_name = "mgmg.model"
	_description = "mgmg.model.sample"
	_inherit = ['mail.thread', 'mail.activity.mixin']

	cv_image = fields.Binary(string="CV_Image", required="True")

	job_type = fields.Selection([
		('odoo developer', 'ODOO Developer'),
		('software developer', 'Software Developer'),
		('content writer', 'Content Writer'),
	], string="Job_Type", default="content writer", required="True")

	name = fields.Char(string="Name")
	dob = fields.Date(string="DOB")
	pob = fields.Char(string="POB")
	sex = fields.Selection([
		('male', 'Male'),
		('female', 'Female'),
		('other', 'Other'),
	], string="Sex", default="other", required="True")
	religion = fields.Char(string="Religion")
	race = fields.Char(string="Race")
	nationality = fields.Char(string="Nationality")
	martial_status = fields.Selection([
		('single', 'Single'),
		('married', 'Married'),
		('relationship', 'Relationship'),
	], string="Martial_Status", default="single", required="True")
	education = fields.Char(string="Education")
	working_experience = fields.Char(string="Working_Experience")
	phone = fields.Integer(string="Phone")