import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let ob = {};
  try {
    ob = {
      'photo': await uploadPhoto(),
      'user': await createUser(),
    };
  } catch (err) { ob = {photo: null, user: null}; }
  return ob;
}
