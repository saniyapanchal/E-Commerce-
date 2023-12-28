import { Schema, model } from 'mongoose';

const categorySchema = Schema({
    name: {
        type: String,
        required: true,
    },
    icon: {
        type: String,
    },
    color: { 
        type: String,
    }
})


categorySchema.virtual('id').get(function () {
    return this._id.toHexString();
});

categorySchema.set('toJSON', {
    virtuals : true,
});

export const Category = model('Category', categorySchema);