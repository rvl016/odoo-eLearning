from odoo import api, models, fields

class User( models.Model) :

  _inherit = ['res.users']

  GROUPS_REF = { 'student': 'elearning.group_elearning_student',
    'teacher': 'elearning.group_elearning_teacher',
    'manager': 'elearning.group_elearning_manager',
    'resources': 'elearning.group_elearning_resources' }

  role = fields.Selection( selection = [('student', 'Student'), 
    ('teacher', 'Teacher'), ('manager', 'Manager'), 
    ('resources', 'Resources')])

  @api.model_create_multi
  def create( self, values_list) :
    for values in values_list :
      if values.get( 'role') :
        values = self._append_group( values)
    return super( User, self).create( values_list)


  def write( self, values) :
    if values.get( 'role') :
      values = self._append_group( values)
    return super( User, self).write( values)

  def _append_group( self, values) :
    group_ref = self.GROUPS_REF[values['role']]
    values['groups_id'] = [(5, 0, 0), (4, self.env.ref( group_ref).id)]
    return values