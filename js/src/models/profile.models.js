import mongoose, { Schema } from "mongoose";

const profileSchema = new Schema(
    {
        name: {
            required: true,
            type: String,
        }
    },
    {
        timestamps:true,
    }
);

const Profile = mongoose.models.Profile || mongoose.model("Profile", profileSchema);

export default Profile;