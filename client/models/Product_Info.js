const { Schema, model } = require("mongoose");

const ProductInfoSchema = new Schema({
  prod_name: {
    type: String,
    trim: true,
  },

  brand: {
    type: String,
    trim: true,
  },

  source: {
    type: String,
  },

  list_price: {
    type: String,
  },

  sale_price: {
    type: String,
  },

  description: {
    type: String,
  },

  review: {
    type: String,
  },

  num_reviews: {
    type: String,
  },

  reviews: [
    {
      type: Schema.Types.ObjectId,
      ref: "Reviews",
    },
  ],
});

const Product_Info = model("Product_Info", ProductInfoSchema);

module.exports = Product_Info;
