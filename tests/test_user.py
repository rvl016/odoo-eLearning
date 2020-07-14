from odoo.tests.common import TransactionCase


class TestUser( TransactionCase) :

  def test_create_user_works( self) :
    User = self.env['res.users']
    user_student = User.create( 
      { 'name': 'Student', 'login': 'student', 'role': 'student' })
    group_rec = self.env.ref( User.GROUPS_REF['student'])
    self.assertEqual( user_student.groups_id, group_rec)

  def test_write_user_works( self) :
    User = self.env['res.users']
    user_resources = User.create( 
      { 'name': 'Resource', 'login': 'resource', 'role': 'student' })
    user_resources.write( { 'role': 'resources' })
    group_rec = self.env.ref( User.GROUPS_REF['resources'])
    self.assertEqual( user_resources.groups_id, group_rec)