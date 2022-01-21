const { Schema, model } = require("mongoose");

const ReviewSchema = new Schema({
  review_id: {
    type: String,
    allowNull: false,
  },

  title: {
    type: String,
  },

  date: {
    type: String,
  },

  rating: {
    type: String,
  },

  text: {
    type: String,
  },
});

const Review = model("Review", ReviewSchema);

module.exports = Review;
