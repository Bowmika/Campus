from odoo import models ,fields


class student(models.Model):
    _name = "student.student"

    name = fields.Char(string="Name")
    roll_no = fields.Integer(string="Roll No")
    student_date_od_birth = fields.Integer("Student date of birth")
    present_days = fields.Integer(string="Present Days")
    absent_days = fields.Date(string="Absent Days")



