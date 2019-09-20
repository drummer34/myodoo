# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Movement(models.Model):
    _name = 'card.movement'

    trackDateTime = fields.Datetime(string="Track Time")

    device_id = fields.Many2one('card.device', string="Device")                 #Bir turnike(device) var, ama çok hareket var [Bir device da birden çok hareket olabilir.]
    object_id = fields.Many2one('card.deviceobject', string="Device Object")    #Bir kartta(objede), birden çok hareket olabilir.


class Device(models.Model):
    _name = 'card.device'
    _rec_name = 'ip_address'            #   Cihaz Tanımlama Ekranı / "card.device,1" yerine, verilen attribute olan "162123123" veya "123213" gelecektir.

    ip_address = fields.Char(string="Ip Address")
    direction = fields.Char(string="3 Selection")
    image_location = fields.Binary(related="location_id.image")

    movement_ids = fields.One2many('card.movement', 'device_id', string="Movement")     # Birden çok hareket, bir device'da olabilir.
    location_id = fields.Many2one('card.location', string="Location")           #Bir lokasyon(turnike) var, ama çok kart var.

class Location(models.Model):
    _name = 'card.location'

    name = fields.Char(string="Location Name")
    image = fields.Binary(string="Image")

    device_ids = fields.One2many('card.device', 'location_id', string="Device")   #Yukardaki ilişkinin ters tanımı

class DeviceObject(models.Model):
    _name = 'card.deviceobject'

    name = fields.Char(string="Device Object Name")
    iot_code = fields.Char(string="IOT Code")

    movement_ids = fields.One2many('card.movement', 'object_id', string="Movement")
    partner_id = fields.Many2one(
        'res.partner',
        delegate=True,
        ondelete='cascade',
        required=True)

class Authorization(models.Model):
    _name = 'card.authorization'

    expire_date = fields.Datetime(string="Expire Date")

    @api.multi
    def check_button(self):
        return True