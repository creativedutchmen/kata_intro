class Game:
    """
    Simple bowling game class to demonstrate TDD in Python
    """

    def __init__(self):
        self._frames = []
        self._rules = [
            RegularRule(),
            SpareRule(),
            StrikeRule(),
        ]

    def add_frame(self, frame):
        frames = list(self._frames)
        frames.append(frame)
        for rule in self._rules:
            rule.check_valid(frames)
        self._frames = frames

    def score(self):
        score = 0
        for rule in self._rules:
            score += rule.calculate_score(self._frames)
        return score


class Scorer(object):
    """
    Abstract Scorer class, to be implemented by all Rules
    """
    def calculate_score(self, frames):
        raise NotImplementedError()


class Validator(object):
    """
    Abstract Validator class, to be implemented by all Rules
    """
    def check_valid(self, frames):
        raise NotImplementedError()


class Rule(Scorer, Validator):
    """
    Abstract Rule class, to be implemented by all Rules
    """
    pass


class FillBallValidator(Validator):
    """
    Abstract class implementing the fill ball rule
    """
    def check_valid(self, frames):
        for index, frame in enumerate(frames):
            if len(frame) > 2 and index != 9:
                raise ValueError('Fill ball only allowed in the last frame')
            if len(frame) > 2 and (frame[0] + frame[1]) < 10:
                raise ValueError('There is no fill ball with an open frame')


class RegularRule(Rule):
    def check_valid(self, frames):
        if not(0 < len(frames) <= 10):
            raise ValueError('Game lasts for a maximum of 10 frames')
        if max([max(frame) for frame in frames]) > 10:
            raise ValueError('There are only ten pins')
        if min([min(frame) for frame in frames]) < 0:
            raise ValueError('You can\'t knock over negative pins')
        return True

    def calculate_score(self, frames):
        score = 0
        for frame in frames:
            score += sum(frame)
        return score


class SpareRule(FillBallValidator, Rule):
    def calculate_score(self, frames):
        score = 0
        for index, frame in enumerate(frames):
            if sum(frame) == 10:
                try:
                    score += frames[index + 1][0]
                except IndexError:
                    pass
        return score


class StrikeRule(FillBallValidator, Rule):
    def check_valid(self, frames):
        # Run the valid check on the parent
        super(StrikeRule, self).check_valid(frames)
        for index, frame in enumerate(frames):
            if ((frame[0] + frame[1]) > 10) and index != 9:
                raise ValueError('If you throw a strike your frame is over')

    def calculate_score(self, frames):
        score = 0
        for index, frame in enumerate(frames):
            if frame[0] == 10:
                try:
                    score += frames[index + 1][1]
                    if frames[index + 1][0] == 10:
                        score += frames[index + 2][0]
                except IndexError:
                    pass
        return score
