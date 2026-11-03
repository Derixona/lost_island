"""Unit tests for deterministic Lost Island game rules."""

import unittest
from game import new_game, available_actions, apply_action, is_win


class LostIslandTests(unittest.TestCase):
    def test_starting_state(self):
        player = new_game("Ada")
        self.assertEqual(player["energy"], 5)
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["inventory"], [])
        self.assertFalse(is_win(player))

    def test_rope_collected_only_once(self):
        player = new_game()
        apply_action(player, "beach")
        apply_action(player, "beach")
        self.assertEqual(player["inventory"], ["rope"])

    def test_jungle_collects_lantern_and_uses_energy(self):
        player = new_game()
        apply_action(player, "jungle")
        self.assertIn("lantern", player["inventory"])
        self.assertEqual(player["energy"], 4)

    def test_bridge_requires_rope(self):
        player = new_game()
        apply_action(player, "bridge")
        self.assertFalse(player["bridge_crossed"])
        self.assertEqual(player["energy"], 5)

    def test_bridge_crossing_only_charges_once(self):
        player = new_game()
        apply_action(player, "beach")
        apply_action(player, "bridge")
        apply_action(player, "bridge")
        self.assertTrue(player["bridge_crossed"])
        self.assertEqual(player["energy"], 4)

    def test_lighthouse_requires_both_prerequisites(self):
        player = new_game()
        apply_action(player, "jungle")
        apply_action(player, "lighthouse")
        self.assertFalse(is_win(player))
        apply_action(player, "beach")
        apply_action(player, "bridge")
        apply_action(player, "lighthouse")
        self.assertTrue(is_win(player))
        self.assertTrue(player["game_over"])

    def test_cave_return_costs_no_energy(self):
        player = new_game()
        apply_action(player, "cave")
        apply_action(player, "return_to_safety")
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)

    def test_cave_loss_never_negative(self):
        player = new_game()
        apply_action(player, "cave")
        for _ in range(5):
            apply_action(player, "explore_deeper")
        self.assertEqual(player["energy"], 0)
        self.assertTrue(player["game_over"])
        apply_action(player, "explore_deeper")
        self.assertEqual(player["energy"], 0)

    def test_invalid_action_does_not_change_state(self):
        player = new_game()
        before = (player["energy"], player["location"], player["inventory"][:])
        apply_action(player, "banana")
        self.assertEqual(before, (player["energy"], player["location"], player["inventory"]))

    def test_cave_actions_are_contextual(self):
        player = new_game()
        apply_action(player, "cave")
        self.assertIn("explore_deeper", available_actions(player))
        self.assertNotIn("bridge", available_actions(player))

    def test_new_game_resets_all_state(self):
        old = new_game()
        apply_action(old, "beach")
        fresh = new_game()
        self.assertEqual(fresh["inventory"], [])
        self.assertEqual(fresh["energy"], 5)
        self.assertFalse(fresh["bridge_crossed"])

    def test_quit(self):
        player = new_game()
        apply_action(player, "quit")
        self.assertTrue(player["quit"])
        self.assertTrue(player["game_over"])
        self.assertFalse(player["won"])


if __name__ == "__main__":
    unittest.main()