# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from flectra import models, api


class ReportFeesAnalysis(models.AbstractModel):
    _name = 'report.openeducat_fees.report_fees_analysis'

    def get_total_amount(self, student_id):
        total_amount = 0.0
        for fees in student_id.fees_detail_ids:
            total_amount += fees.amount
        return total_amount

    def get_total_left(self, student_id):
        total_left = 0.0
        for fees in student_id.fees_detail_ids:
            if not fees.invoice_state == 'paid':
                total_left += fees.amount
        return total_left

    @api.model
    def get_report_values(self, docids, data=None):
        student_ids = []
        if data['fees_filter'] == 'student':
            student_ids = self.env['op.student'].browse([data['student']])
        else:
            student_ids = self.env['op.student'].search(
                [('course_detail_ids.course_id', '=', data['course'])])

        docargs = {
            'doc_ids': self.ids,
            'doc_model': 'op.student',
            'docs': student_ids,
            'get_total_amount': self.get_total_amount,
            'get_total_left': self.get_total_left,
        }
        return docargs
