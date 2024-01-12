import { Schema } from "mongoose";
import mongoose from "mongoose";

const imageSchema = new Schema(
    {
        url: {
            required: true,
            type: String,
        },
        profile: {
            type: mongoose.Schema.Types.ObjectId,
            ref: "Profile",
            required: true,
        }
    },
    {
        timestamps:true
    }
);

const Image = mongoose.models.Image || mongoose.model("Image", imageSchema);

export default Image;