import higher_lower

user_is_correct = True
user_score = 0
instagram_user_a = higher_lower.get_random_instagram_user()
instagram_user_b = higher_lower.get_random_instagram_user()

while user_is_correct:
    higher_lower.clear_screen()
    higher_lower.print_logo()
    higher_lower.print_current_score(user_score)
    higher_lower.print_question(instagram_user_a, instagram_user_b)

    user_answer = higher_lower.get_user_answer()
    highest_followers = higher_lower.calculate_highest_followers(
        instagram_user_a['follower_count'], instagram_user_b['follower_count'])

    if user_answer.upper() == highest_followers:
        user_score += 1
        instagram_user_a = instagram_user_b
        instagram_user_b = higher_lower.get_random_instagram_user()
    else:
        user_is_correct = False

higher_lower.clear_screen()
higher_lower.print_logo()
higher_lower.print_final_score(user_score)
