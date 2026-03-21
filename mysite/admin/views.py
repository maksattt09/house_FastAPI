from sqladmin import ModelView
from mysite.database.models import UserProfile, Property, Review


class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [UserProfile.id, UserProfile.first_name, UserProfile.last_name, UserProfile.username,
        UserProfile.email, UserProfile.role, UserProfile.preferred_language]


class PropertyAdmin(ModelView, model=Property):
    column_list = [Property.id, Property.tittle, Property.property_type, Property.region, Property.city,
        Property.price, Property.rooms, Property.seller_id]


class ReviewAdmin(ModelView, model=Review):
    column_list = [Review.id, Review.author_id, Review.seller_rev_id, Review.rating, Review.comment,
                   Review.created_at]

