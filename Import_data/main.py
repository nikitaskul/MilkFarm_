from pprint import pprint
import utils


if __name__ == '__main__':

    result = utils.get_sorted_data()
    pprint(result[0])

    i = 1
    for profile in result:
        user = utils.prepare_user_info(profile)
        try:
            user.save()
        except Exception:
            print(i)

        if i % 100 == 0:
            print(i)
        i += 1
