from odoo import models, fields, _, api
from odoo.exceptions import ValidationError
class AccountReport(models.Model):
    _inherit = 'account.report'

    hide_initial_balance = fields.Boolean(
        string="Initial Balance", default=False
    )

    def _init_options_initial_balance(self, options, previous_options=None):
        '''
        Initialize a filter based on the initial_balance of the line (hide).
        '''
        options['initial_balance'] = [
            {'id': 'hide', 'name': _("hide"), 'selected': False}
        ]
        
        if previous_options and previous_options.get('initial_balance'):
            previously_selected_ids = {x['id'] for x in previous_options['initial_balance'] if x.get('selected')}
            for opt in options['initial_balance']:
                opt['selected'] = opt['id'] in previously_selected_ids

        selected_options = {x['id']: x['name'] for x in options['initial_balance'] if x['selected']}
        selected_ids = set(selected_options.keys())
        display_names = []

        for sel in selected_ids:
            display_names.append(selected_options.get(sel))
        options['initial_balance_display_name'] = ', '.join(display_names)



        
    @api.model
    def _get_options_initial_balance(self, options):

        if not options.get('initial_balance') or len(options.get('initial_balance')) == 0:
            return []
        for opt in options.get('initial_balance'):
            if opt['id'] == 'hide' and opt['selected'] == True:
                self.hide_initial_balance = True
                print(f"{self.hide_initial_balance} ---------------------")
            else:
                self.hide_initial_balance = False

        

    def _get_partner_and_general_ledger_initial_balance_line(self, options, parent_line_id, eval_dict, account_currency=None, level_shift=0):
        self._get_options_initial_balance(options)
        print(f"{self.hide_initial_balance}")
        if self.hide_initial_balance == True:
            return[]
        else :
            return super(AccountReport,self)._get_partner_and_general_ledger_initial_balance_line(options, parent_line_id, eval_dict, account_currency=None, level_shift=0)
