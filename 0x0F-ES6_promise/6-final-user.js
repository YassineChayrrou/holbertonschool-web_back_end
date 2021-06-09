import uploadPhoto from './5-photo-reject';
import signUpUser from './4-user-promise';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const array = [];
  const signedUser = await signUpUser(firstName, lastName).then((data) => ({
    status: 'fulfilled',
    value: data,
  }));

  const profilePhoto = await uploadPhoto(fileName).catch((error) => ({
    status: 'rejected',
    value: error.toString(),
  }));
  return [signedUser, profilePhoto];
}
