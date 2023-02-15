# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
# from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class firstWebsite(http.Controller):

    # voici le controller de page d'acceuil
    @http.route('/home', website=True, type="http", auth="public", csrf=False)
    def home(self, **kwargs):
        print(kwargs)
        prop__items = http.request.env['estate.property'].sudo().search([])
        return request.render('estate.properties_details', {
            'properties': prop__items,
            'pays': http.request.env['res.country'].sudo().search([]),
            'prop_type': http.request.env['estate.property.type'].sudo().search([]),
        })

    # available_properties
    @http.route("/properties/available", website=True, type="http", auth="public", csrf=False)
    def properties_available(self, **kwargs):
        print(kwargs)
        pays = request.env['res.country'].sudo().search([('name', '=', kwargs.get('pays'))])
        prop_type = request.env['estate.property.type'].sudo().search([('name', '=', kwargs.get('property_type'))])
        # _logger.info("################## ALMAREX #############")
        # _logger.info(kwargs.get('property_status'))
        property_existe = request.env['estate.property'].sudo().search([
            ('country', '=', pays.id),
            "|", ('type', '=', prop_type.id),
            ('state', '=', kwargs.get('property_status'))
        ])
        _logger.info("################## RECHERCHE KARIDIOULA #############")
        _logger.info(property_existe)
        # raise ValidationError("erreur ici")
        return http.request.render("estate.available_properties", {
            "estate_properties": property_existe,
            'prop_type': http.request.env['estate.property.type'].sudo().search([]),
        })

    @http.route('/properties/available/<model("estate.property"):name>/', website=True, type="http", auth="public",
                csrf=False)
    def props(self, name):
        product_details = http.request.env['estate.property'].sudo().search([('id', '=', name.id)])
        return http.request.render('estate.product_details', {
            'props': product_details
        })

    # page d'apropos
    @http.route("/about", website=True, type="http", auth="public", csrf=False)
    def about(self, **kwargs):
        print(kwargs)
        return http.request.render('estate.about_template_page_id')

    # contact page
    @http.route("/contact", website=True, type="http", auth="public", csrf=False)
    def contact(self, **kwargs):
        print(kwargs)
        return http.request.render('estate.contact_template_page_id', {})

