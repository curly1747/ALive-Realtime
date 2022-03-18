from flask_config import db, Session
from sqlalchemy import ForeignKeyConstraint


class Package(db.Model):
    __tablename__ = 'mission_package_info'
    __table_args__ = {
        'autoload': True,
        'schema': 'gami',
        'autoload_with': db.engine
    }


class UserPackage(db.Model):
    __tablename__ = 'user_package'
    __table_args__ = {
        'autoload': True,
        'schema': 'gami',
        'autoload_with': db.engine
    }


class RewardInfo(db.Model):
    __tablename__ = 'reward_info'
    __table_args__ = {
        'autoload': True,
        'schema': 'gami',
        'autoload_with': db.engine
    }


class SourceInfo(db.Model):
    __tablename__ = 'gsource'
    __table_args__ = {
        'autoload': True,
        'schema': 'gami',
        'autoload_with': db.engine
    }


class RewardHistory(db.Model):
    __tablename__ = 'reward_audit_log'
    __table_args__ = {
        'autoload': True,
        'schema': 'gami',
        'autoload_with': db.engine
    }


class Transactions(db.Model):
    __tablename__ = 'transactions'
    __table_args__ = {
        'autoload': True,
        'schema': 'wallet',
        'autoload_with': db.engine
    }


class LootboxReward(db.Model):
    __tablename__ = 'user_box_consume_history'
    __table_args__ = {
        'autoload': True,
        'schema': 'gami',
        'autoload_with': db.engine
    }


class LootboxHistory(db.Model):
    __tablename__ = 'reward_loot_box_history'
    __table_args__ = {
        'autoload': True,
        'schema': 'gami',
        'autoload_with': db.engine
    }


class RewardDiamondHistory(db.Model):
    __tablename__ = 'reward_diamond_history'
    __table_args__ = {
        'autoload': True,
        'schema': 'gami',
        'autoload_with': db.engine
    }


class Diamond(db.Model):
    __tablename__ = 'diamond'
    __table_args__ = {
        'autoload': True,
        'schema': 'wallet',
        'autoload_with': db.engine
    }


class FCMToken(db.Model):
    __tablename__ = 'user_token'
    __table_args__ = {
        'autoload': True,
        'schema': 'fcm_token',
        'autoload_with': db.engine
    }


class ItemInfo(db.Model):
    __tablename__ = 'item'
    __table_args__ = {
        'autoload': True,
        'schema': 'gami',
        'autoload_with': db.engine
    }


class UserMaterial(db.Model):
    __tablename__ = 'user_mission_material'
    __table_args__ = {
        'autoload': True,
        'schema': 'gami',
        'autoload_with': db.engine
    }


class SendGiftHistory(db.Model):
    __tablename__ = 'send_gift_history'
    __table_args__ = {
        'autoload': True,
        'schema': 'wallet',
        'autoload_with': db.engine
    }


class Idol(db.Model):
    __tablename__ = 'idol'
    __table_args__ = {
        'autoload': True,
        'schema': 'agency',
        'autoload_with': db.engine
    }


class IdolRegistry(db.Model):
    __tablename__ = 'idol_register_history'
    __table_args__ = {
        'autoload': True,
        'schema': 'agency',
        'autoload_with': db.engine
    }


class PhongThanHistory(db.Model):
    __tablename__ = 'reward_evipoint_history'
    __table_args__ = {
        'autoload': True,
        'schema': 'gami',
        'autoload_with': db.engine
    }


class PhongThanRewardConfig(db.Model):
    __tablename__ = 'reward_evipoint_ranking_config'
    __table_args__ = {
        'autoload': True,
        'schema': 'gami',
        'autoload_with': db.engine
    }


class IdolStarRanking1D(db.Model):
    __tablename__ = 'idol_star_ranking_1d'
    __table_args__ = {
        'autoload': True,
        'schema': 'wallet',
        'autoload_with': db.engine
    }
