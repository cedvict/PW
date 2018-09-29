# © 2016 Serpent Consulting Services Pvt. Ltd. (support@serpentcs.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Mass Editing',
    'version': '2.0.0',
    'author': """BetaPy,
              Serpent Consulting Services Pvt. Ltd.,
              Odoo Community Association (OCA)""",
    'contributors': [
        'Oihane Crucelaegui <oihanecrucelaegi@gmail.com>',
        'Serpent Consulting Services Pvt. Ltd. <support@serpentcs.com>',
        'Jay Vora <jay.vora@serpentcs.com>'
    ],
    'category': 'Tools',
    "website": "https://betapy.com",
    "support": "incoming+betapy/support@incoming.gitlab.com",
    'license': 'AGPL-3',
    'summary': 'Mass Editing',
    'uninstall_hook': 'uninstall_hook',
    'depends': [
        'base',
    ],
    'images': "static/description/banner.jpg",
    'data': [
        'security/ir.model.access.csv',
        'views/mass_editing_view.xml',
        'views/template.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
